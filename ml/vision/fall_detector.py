def detect_fall(keypoints: dict[str, tuple[float, float]]) -> float:
    shoulder_y = keypoints.get("shoulder", (0.0, 0.0))[1]
    hip_y = keypoints.get("hip", (0.0, 0.0))[1]
    ankle_y = keypoints.get("ankle", (0.0, 0.0))[1]
    body_span = abs(ankle_y - shoulder_y)
    torso_tilt = abs(hip_y - shoulder_y)

    if body_span < 0.18 and torso_tilt < 0.08:
        return 0.82
    if body_span < 0.30:
        return 0.63
    return 0.18

