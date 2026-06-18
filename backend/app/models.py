from dataclasses import dataclass
from enum import Enum
from typing import Literal


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(frozen=True)
class AudioEvent:
    event_id: str
    household_id: str
    label: str
    confidence: float
    started_at: str
    duration_sec: float
    snr: float


@dataclass(frozen=True)
class VisionSignal:
    household_id: str
    fall_probability: float
    stillness_sec: int
    camera_zone: str


@dataclass(frozen=True)
class FusedIncident:
    event_id: str
    household_id: str
    title: str
    level: RiskLevel
    score: float
    action: Literal["watch", "notify_family", "dispatch_staff", "call_emergency"]
    evidence: list[str]

