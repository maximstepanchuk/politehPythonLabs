from point import Point
from math import sqrt
class Segment(Point):
    def __init__(self, coordinateX, coordinateY, coordinateZ, coordinateX2, coordinateY2, coordinateZ2):
        super().__init__(coordinateX, coordinateY, coordinateZ)
        self.x2 = coordinateX2
        self.y2 = coordinateY2
        self.z2 = coordinateZ2

    def find_length(self) -> float:
        return sqrt((pow(2, (self.x2-self._x))) + (pow(2, (self.y2 - self._y)))+(pow(2, (self.z2 - self._z))))
