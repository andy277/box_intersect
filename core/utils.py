from typing import Tuple


class Box:
    def intersection(self, rect1: Tuple[float, ...], rect2: Tuple[float, ...]) -> float:
        rect1_xmax = rect1[0] + rect1[2] / 2
        rect2_xmax = rect2[0] + rect2[2] / 2
        rect1_xmin = rect1[0] - rect1[2] / 2
        rect2_xmin = rect2[0] - rect2[2] / 2

        rect1_ymax = rect1[1] + rect1[2] / 2
        rect2_ymax = rect2[1] + rect2[2] / 2
        rect1_ymin = rect1[1] - rect1[2] / 2
        rect2_ymin = rect2[1] - rect2[2] / 2

        dx = min(rect1_xmax, rect2_xmax) - max(rect1_xmin, rect2_xmin)
        dy = min(rect1_ymax, rect2_ymax) - max(rect1_ymin, rect2_ymin)

        if dx >= 0 and dy >= 0:
            return dx * dy

    def total_area(self, rect1: Tuple[float, ...], rect2: Tuple[float, ...]) -> float:
        rect1_area = rect1[2] * rect1[3]
        rect2_area = rect2[2] * rect2[3]

        return rect1_area + rect2_area
