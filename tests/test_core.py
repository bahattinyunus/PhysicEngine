import unittest
import sys
import os

# src dizinini path'e ekle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.vector import Vector2D
from src.core.body import Body
from src.core.engine import Engine

class TestPhysicEngine(unittest.TestCase):
    def test_vector_addition(self):
        v1 = Vector2D(1, 2)
        v2 = Vector2D(3, 4)
        result = v1 + v2
        self.assertEqual(result.x, 4)
        self.assertEqual(result.y, 6)

    def test_body_gravity(self):
        engine = Engine(gravity=Vector2D(0, 10))
        body = Body(mass=1.0, position=Vector2D(0, 0))
        engine.add_body(body)
        
        # 1 saniye sonra serbest düşüş: y = 0.5 * g * t^2 = 5
        # Semi-implicit Euler'de: v = v0 + g*dt, p = p0 + v*dt
        # dt=1 için: v = 10, p = 10
        engine.step(1.0)
        self.assertEqual(body.position.y, 10)
        self.assertEqual(body.velocity.y, 10)

if __name__ == '__main__':
    unittest.main()
