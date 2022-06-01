import Rectangle
class Parallelepiped(Rectangle):
    def __init__(self, parallelepiped_height, height, width):
        self._height = parallelepiped_height
        super().__init__(height, width)
