
from typing import Dict, List, Union
from datetime import datetime, timedelta

class PerformanceAnalyzer:
    def __init__(self):
        self.metrics: Dict[str, Dict[str, Union[int, float]]] = {}

    def add_metric(self, content_id: str, metric_name: str, value: Union[int, float]) -> None:
        # Implementation details here
        pass

    def get_top_performing_content(self, metric: str, limit: int = 10) -> List[Dict[str, Union[str, int, float]]]:
        # Implementation details here
        pass

    def calculate_engagement_rate(self, content_id: str) -> float:
        # Implementation details here
        pass

    def get_performance_trend(self, content_id: str, days: int = 7) -> Dict[str, List[float]]:
        # Implementation details here
        pass

if __name__ == "__main__":
    # Example usage
    analyzer = PerformanceAnalyzer()
    # Add example usage here
