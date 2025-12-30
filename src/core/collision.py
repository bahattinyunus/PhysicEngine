from .vector import Vector2D
from .shapes import ShapeType
import math

class Manifold:
    """Çarpışma verilerini (normal, derinlik vb.) saklayan sınıf."""
    def __init__(self, body_a, body_b):
        self.body_a = body_a
        self.body_b = body_b
        self.penetration = 0.0
        self.normal = Vector2D()

def solve_collision(manifold):
    """İki gövde arasındaki çarpışmayı tespit eder ve manifold bilgilerini doldurur."""
    a = manifold.body_a
    b = manifold.body_b
    
    if not a.shape or not b.shape:
        return False

    # Circle vs Circle
    if a.shape.type == ShapeType.CIRCLE and b.shape.type == ShapeType.CIRCLE:
        return solve_circle_vs_circle(manifold)
    
    # Circle vs AABB
    if a.shape.type == ShapeType.CIRCLE and b.shape.type == ShapeType.AABB:
        return solve_circle_vs_aabb(manifold)
    
    # AABB vs Circle
    if a.shape.type == ShapeType.AABB and b.shape.type == ShapeType.CIRCLE:
        # Manifold'ı ters çevirip aynı mantığı kullan
        manifold.body_a, manifold.body_b = b, a
        result = solve_circle_vs_aabb(manifold)
        manifold.normal = manifold.normal * -1.0
        return result

def solve_circle_vs_circle(manifold):
    a = manifold.body_a
    b = manifold.body_b
    
    direction = b.position - a.position
    distance_sq = direction.magnitude_sq()
    radius_sum = a.shape.radius + b.shape.radius
    
    if distance_sq >= radius_sum**2:
        return False
        
    distance = math.sqrt(distance_sq)
    manifold.penetration = radius_sum - distance
    
    if distance == 0:
        manifold.normal = Vector2D(1, 0)
    else:
        manifold.normal = direction * (1.0 / distance)
        
    return True

def solve_circle_vs_aabb(manifold):
    circle = manifold.body_a
    aabb = manifold.body_b
    
    # Daire merkezinden AABB merkezine olan vektör
    n = circle.position - aabb.position
    
    # AABB üzerindeki en yakın noktayı bul (Clamp)
    closest = Vector2D(n.x, n.y)
    closest.x = max(-aabb.shape.half_width, min(aabb.shape.half_width, closest.x))
    closest.y = max(-aabb.shape.half_height, min(aabb.shape.half_height, closest.y))
    
    inside = False
    
    # Daire merkezi AABB içindeyse
    if n.x == closest.x and n.y == closest.y:
        inside = True
        
        # En yakın kenarı bul
        if abs(n.x) > abs(n.y):
            if closest.x > 0: closest.x = aabb.shape.half_width
            else: closest.x = -aabb.shape.half_width
        else:
            if closest.y > 0: closest.y = aabb.shape.half_height
            else: closest.y = -aabb.shape.half_height
            
    normal = n - closest
    d_sq = normal.magnitude_sq()
    radius = circle.shape.radius
    
    if d_sq > radius**2 and not inside:
        return False
        
    distance = math.sqrt(d_sq)
    
    if inside:
        manifold.normal = normal.normalize() * -1.0 if d_sq > 0 else Vector2D(1, 0)
        manifold.penetration = radius + distance
    else:
        manifold.normal = normal.normalize() if d_sq > 0 else Vector2D(1, 0)
        manifold.penetration = radius - distance
        
    return True
