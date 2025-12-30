from .vector import Vector2D

class Body:
    """Fiziksel bir nesneyi (rijit gövde) temsil eden sınıf."""
    def __init__(self, mass=1.0, position=None, velocity=None, shape=None):
        self.mass = float(mass)
        self.inv_mass = 1.0 / mass if mass > 0 else 0.0
        self.position = position if position else Vector2D()
        self.velocity = velocity if velocity else Vector2D()
        self.acceleration = Vector2D()
        self.force_accumulator = Vector2D()
        self.shape = shape
        self.restitution = 0.5 # Geri sekme katsayısı (0=yapışkan, 1=tam esnek)

    def apply_force(self, force):
        """Nesneye kuvvet uygular."""
        self.force_accumulator += force

    def clear_forces(self):
        """Kuvvet biriktiriciyi sıfırlar."""
        self.force_accumulator = Vector2D()

    def integrate(self, dt):
        """Nesnenin durumunu zaman adımı (dt) kadar günceller. (Semi-implicit Euler)"""
        # ivme = kuvvet / kütle
        self.acceleration = self.force_accumulator * self.inv_mass
        
        # Hız güncelleme
        self.velocity += self.acceleration * dt
        
        # Pozisyon güncelleme
        self.position += self.velocity * dt
        
        self.clear_forces()

    def __repr__(self):
        return f"Body(mass={self.mass}, pos={self.position}, vel={self.velocity})"
