from math import sqrt
class Point:
    def __init__(self, coordinateX, coordinateY, coordinateZ):
        self._x = coordinateX
        self._y = coordinateY
        self._z = coordinateZ


class Segment(Point):
    def __init__(self, coordinateX, coordinateY, coordinateZ, coordinateX2, coordinateY2, coordinateZ2):
        super().__init__(coordinateX, coordinateY, coordinateZ)
        self.x2 = coordinateX2
        self.y2 = coordinateY2
        self.z2 = coordinateZ2

    def find_length(self) -> float:
        return sqrt((pow(2, (self.x2-self._x))) + (pow(2, (self.y2 - self._y)))+(pow(2, (self.z2 - self._z))))


class Circle:
    def __init__(self):
        self._radius = r


class Sphere(Circle):
    def __init__(self, radius):
        super().__init__(radius)


class Rectangle:
    def __init__(self, rectangle_height, rectangle_width):
        self._height = rectangle_height
        self._width = rectangle_width

    def get_square(self) -> float:
        return self._width * self._height

class Parallelepiped(Rectangle):
    def __init__(self, parallelepiped_height, height, width):
        self._height = parallelepiped_height
        super().__init__(height, width)

segment = Segment(7,8,5,6,9,3)
print(segment.find_length())