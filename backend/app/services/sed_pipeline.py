from dataclasses import dataclass


@dataclass(frozen=True)
class SedPrediction:
    label: str
    confidence: float
    onset: float
    offset: float


class SedPipeline:
    labels = ["日常谈话", "呼救", "尖叫", "烟雾报警器", "跌倒撞击", "水流声"]

    def predict(self, rms: float, zero_crossing_rate: float, band_energy: float) -> SedPrediction:
        if band_energy > 0.82 and zero_crossing_rate > 0.45:
            return SedPrediction("尖叫", 0.91, 0.4, 2.8)
        if rms > 0.78 and band_energy > 0.58:
            return SedPrediction("跌倒撞击", 0.84, 0.1, 1.2)
        if band_energy > 0.70:
            return SedPrediction("烟雾报警器", 0.88, 0.0, 4.0)
        return SedPrediction("日常谈话", 0.31, 0.0, 1.0)

