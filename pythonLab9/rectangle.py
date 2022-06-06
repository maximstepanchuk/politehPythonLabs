class Rectangle:
    def __init__(self, rectangle_height, rectangle_width):
        self._height = rectangle_height
        self._width = rectangle_width

    def get_square(self) -> float:
        return self._width * self._height
