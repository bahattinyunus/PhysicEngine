from .vector import Vector2D

class Engine:
    """Fizik simülasyonunu yöneten ana motor."""
    def __init__(self, gravity=Vector2D(0, 9.81)):
        self.bodies = []
        self.gravity = gravity

    def add_body(self, body):
        """Simülasyona yeni bir gövde ekler."""
        self.bodies.append(body)

    def step(self, dt):
        """Tüm dünyayı bir zaman adımı ilerletir."""
        for body in self.bodies:
            if body.inv_mass > 0:
                # Yerçekimi uygula
                body.apply_force(self.gravity * body.mass)
            
            # Dinamikleri güncelle
            body.integrate(dt)

    def __repr__(self):
        return f"Engine(bodies={len(self.bodies)}, gravity={self.gravity})"
