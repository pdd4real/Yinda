from typing import Optional

from backend.app.models import AudioEvent, FusedIncident, RiskLevel, VisionSignal


HIGH_RISK_AUDIO = {"呼救", "尖叫", "烟雾报警器", "剧烈撞击", "玻璃破碎"}


def fuse_incident(audio: AudioEvent, vision: Optional[VisionSignal] = None) -> FusedIncident:
    """Fuse audio-first evidence with optional vision signals for dispatch decisions."""
    evidence = [f"声音事件：{audio.label}({audio.confidence:.2f})"]
    score = audio.confidence

    if audio.label in HIGH_RISK_AUDIO:
        score += 0.18

    if audio.duration_sec >= 3:
        score += 0.08
        evidence.append(f"持续时间：{audio.duration_sec:.1f}s")

    if audio.snr < 8:
        score -= 0.06
        evidence.append("低信噪比：已降低单源权重")

    if vision:
        if vision.fall_probability >= 0.65:
            score += 0.22
            evidence.append(f"视频跌倒概率：{vision.fall_probability:.2f}")
        if vision.stillness_sec >= 90:
            score += 0.10
            evidence.append(f"静止时长：{vision.stillness_sec}s")

    score = max(0.0, min(score, 1.0))

    if score >= 0.90:
        level = RiskLevel.CRITICAL
        action = "call_emergency"
    elif score >= 0.76:
        level = RiskLevel.HIGH
        action = "dispatch_staff"
    elif score >= 0.55:
        level = RiskLevel.MEDIUM
        action = "notify_family"
    else:
        level = RiskLevel.LOW
        action = "watch"

    return FusedIncident(
        event_id=audio.event_id,
        household_id=audio.household_id,
        title=f"{audio.label}异常事件",
        level=level,
        score=round(score, 3),
        action=action,
        evidence=evidence,
    )
