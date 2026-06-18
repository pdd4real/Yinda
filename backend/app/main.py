from backend.app.models import AudioEvent, VisionSignal
from backend.app.services.event_fusion import fuse_incident
from backend.app.services.task_dispatch import create_dispatch_task


def demo_incident() -> dict[str, object]:
    audio = AudioEvent(
        event_id="evt-20260615-001",
        household_id="H-032",
        label="呼救",
        confidence=0.86,
        started_at="2026-06-15T20:14:33+08:00",
        duration_sec=4.8,
        snr=12.5,
    )
    vision = VisionSignal("H-032", fall_probability=0.72, stillness_sec=118, camera_zone="客厅")
    incident = fuse_incident(audio, vision)
    task = create_dispatch_task(incident)
    return {"incident": incident, "task": task}


if __name__ == "__main__":
    print(demo_incident())

