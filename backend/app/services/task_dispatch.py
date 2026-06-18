from dataclasses import dataclass
from typing import Optional

from backend.app.models import FusedIncident, RiskLevel


@dataclass(frozen=True)
class DispatchTask:
    task_id: str
    incident_id: str
    assignee_role: str
    deadline_min: int
    message: str


def create_dispatch_task(incident: FusedIncident) -> Optional[DispatchTask]:
    if incident.level == RiskLevel.LOW:
        return None

    if incident.level == RiskLevel.CRITICAL:
        role = "社区值班员 + 120 联动"
        deadline = 2
    elif incident.level == RiskLevel.HIGH:
        role = "社区网格员"
        deadline = 5
    else:
        role = "家属联系人"
        deadline = 15

    return DispatchTask(
        task_id=f"task-{incident.event_id}",
        incident_id=incident.event_id,
        assignee_role=role,
        deadline_min=deadline,
        message=f"{incident.title}，风险分 {incident.score:.2f}，请在 {deadline} 分钟内确认。",
    )
