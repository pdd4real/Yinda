from dataclasses import dataclass
from time import time


@dataclass(frozen=True)
class CapturePacket:
    device_id: str
    household_id: str
    timestamp: float
    audio_path: str
    video_frame_path: str


class EdgeAgent:
    def __init__(self, device_id: str, household_id: str) -> None:
        self.device_id = device_id
        self.household_id = household_id

    def capture_window(self) -> CapturePacket:
        stamp = int(time())
        return CapturePacket(
            device_id=self.device_id,
            household_id=self.household_id,
            timestamp=time(),
            audio_path=f"/var/audiocare/cache/{stamp}.wav",
            video_frame_path=f"/var/audiocare/cache/{stamp}.jpg",
        )

    def heartbeat(self) -> dict[str, object]:
        return {
            "deviceId": self.device_id,
            "householdId": self.household_id,
            "online": True,
            "firmware": "edge-agent/0.4.2",
        }


if __name__ == "__main__":
    agent = EdgeAgent("HK-2CD3T-001", "H-032")
    print(agent.heartbeat())
    print(agent.capture_window())

