import unittest

from backend.app.models import AudioEvent, RiskLevel, VisionSignal
from backend.app.services.event_fusion import fuse_incident
from backend.app.services.task_dispatch import create_dispatch_task


class EventFusionTest(unittest.TestCase):
    def test_audio_and_fall_signal_escalates_to_critical(self):
        audio = AudioEvent("evt-1", "H-1", "呼救", 0.84, "2026-06-15T20:00:00+08:00", 5.2, 14)
        vision = VisionSignal("H-1", 0.74, 120, "客厅")

        incident = fuse_incident(audio, vision)
        task = create_dispatch_task(incident)

        self.assertEqual(incident.level, RiskLevel.CRITICAL)
        self.assertEqual(incident.action, "call_emergency")
        self.assertIsNotNone(task)
        self.assertEqual(task.deadline_min, 2)

    def test_low_confidence_daily_sound_stays_watch_only(self):
        audio = AudioEvent("evt-2", "H-1", "日常谈话", 0.32, "2026-06-15T20:00:00+08:00", 1.1, 22)

        incident = fuse_incident(audio)
        task = create_dispatch_task(incident)

        self.assertEqual(incident.level, RiskLevel.LOW)
        self.assertEqual(incident.action, "watch")
        self.assertIsNone(task)


if __name__ == "__main__":
    unittest.main()

