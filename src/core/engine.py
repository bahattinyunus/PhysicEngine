from .vector import Vector2D
from .collision import Manifold, solve_collision

class Engine:
    """Fizik simülasyonunu yöneten ana motor."""
    def __init__(self, gravity=Vector2D(0, 9.81)):
        self.bodies = []
        self.gravity = gravity

    def add_body(self, body):
        """Simülasyona yeni bir gövde ekler."""
        self.bodies.append(body)

    def step(self, dt, iterations=1):
        """Tüm dünyayı bir zaman adımı ilerletir."""
        # 1. Entegrasyon (Hız ve Konum)
        for body in self.bodies:
            if body.inv_mass > 0:
                body.apply_force(self.gravity * body.mass)
            body.integrate(dt)

        # 2. Çarpışma Tespiti ve Çözümleme
        for _ in range(iterations):
            self.handle_collisions()

    def handle_collisions(self):
        manifolds = []
        for i in range(len(self.bodies)):
            for j in range(i + 1, len(self.bodies)):
                a = self.bodies[i]
                b = self.bodies[j]
                
                if a.inv_mass == 0 and b.inv_mass == 0:
                    continue
                
                manifold = Manifold(a, b)
                if solve_collision(manifold):
                    self.resolve_collision(manifold)
                    self.positional_correction(manifold)

    def resolve_collision(self, manifold):
        a = manifold.body_a
        b = manifold.body_b
        normal = manifold.normal
        
        # Görece hız (Relative velocity)
        rv = b.velocity - a.velocity
        
        # Hızın normal bileşeni
        vel_along_normal = rv.dot(normal)
        
        # Nesneler birbirinden uzaklaşıyorsa işlem yapma
        if vel_along_normal > 0:
            return
            
        # En düşük restitution değerini kullan
        e = min(a.restitution, b.restitution)
        
        # İtme (Impulse) büyüklüğü skaler j
        j = -(1 + e) * vel_along_normal
        j /= (a.inv_mass + b.inv_mass)
        
        # İtmeyi uygula
        impulse = j * normal
        a.velocity -= a.inv_mass * impulse
        b.velocity += b.inv_mass * impulse

    def positional_correction(self, manifold):
        """Nesnelerin birbirinin içine geçmesini engeller (Sinking prevention)."""
        percent = 0.2 # 0.2 to 0.8
        slop = 0.01   # 0.01 to 0.1
        a = manifold.body_a
        b = manifold.body_b
        
        correction = max(manifold.penetration - slop, 0.0) / (a.inv_mass + b.inv_mass) * percent * manifold.normal
        a.position -= a.inv_mass * correction
        b.position += b.inv_mass * correction

    def __repr__(self):
        return f"Engine(bodies={len(self.bodies)}, gravity={self.gravity})"
