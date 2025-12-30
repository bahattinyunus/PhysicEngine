import math

class Vector2D:
    """2D Vektör işlemleri için temel sınıf."""
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def magnitude_sq(self):
        return self.x**2 + self.y**2

    def magnitude(self):
        return math.sqrt(self.magnitude_sq())

    def normalize(self):
        mag = self.magnitude()
        if mag > 0:
            return self * (1.0 / mag)
        return Vector2D(0, 0)

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"
