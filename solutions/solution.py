import abc

import intersection


class Solution(abc.ABC):
    def __init__(self, intersections: dict[int, intersection.Intersection]):
        self.intersections = intersections

    @abc.abstractmethod
    def run(self) -> dict[int, intersection.Intersection]:
        ...
