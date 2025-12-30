from .vector import Vector2D
import math

class ShapeType:
    CIRCLE = 0
    AABB = 1

class Shape:
    """Geometrik şekiller için temel sınıf."""
    def __init__(self, type):
        self.type = type

class Circle(Shape):
    """Daire şekli."""
    def __init__(self, radius):
        super().__init__(ShapeType.CIRCLE)
        self.radius = float(radius)

class AABB(Shape):
    """Eksen Hizalı Sınırlayıcı Kutu (Rectangle)."""
    def __init__(self, width, height):
        super().__init__(ShapeType.AABB)
        self.width = float(width)
        self.height = float(height)
        self.half_width = width / 2.0
        self.half_height = height / 2.0
