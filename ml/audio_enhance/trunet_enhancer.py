def enhance(samples: list[float], noise_floor: float = 0.05) -> list[float]:
    """Suppress small background noise while preserving sharp alarm events."""
    cleaned: list[float] = []
    for sample in samples:
        if abs(sample) < noise_floor:
            cleaned.append(0.0)
        else:
            cleaned.append(max(-1.0, min(1.0, sample * 1.12)))
    return cleaned

