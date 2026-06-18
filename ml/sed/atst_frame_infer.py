class ATSTFrameClassifier:
    """Lightweight placeholder for the ATST-Frame fine-tuned SED model."""

    def __init__(self, threshold: float = 0.62) -> None:
        self.threshold = threshold

    def classify(self, frame_features: list[float]) -> dict[str, float | str]:
        energy = sum(frame_features) / max(len(frame_features), 1)
        if energy > 0.82:
            return {"label": "尖叫", "confidence": 0.93}
        if energy > self.threshold:
            return {"label": "呼救", "confidence": 0.86}
        return {"label": "日常活动", "confidence": 0.38}

