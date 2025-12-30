import sys
import os

# src dizinini path'e ekle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.vector import Vector2D
from src.core.body import Body
from src.core.engine import Engine
from src.core.shapes import Circle, AABB
import time

def run_collision_demo():
    # Motoru başlat (Yerçekimi kapatıldı - Saf çarpışma testi için)
    engine = Engine(gravity=Vector2D(0, 0))

    # İki top oluştur (Birbirine doğru hareket eden)
    ball1 = Body(mass=1.0, position=Vector2D(0, 0), velocity=Vector2D(5, 0), shape=Circle(radius=1.0))
    ball2 = Body(mass=1.0, position=Vector2D(5, 0.5), velocity=Vector2D(-5, 0), shape=Circle(radius=1.0))
    
    # Restitution ayarla (Esneklik)
    ball1.restitution = 0.8
    ball2.restitution = 0.8 / 2 # ball2'nin restitution değerini düşürelim

    engine.add_body(ball1)
    engine.add_body(ball2)

    print("--- Çarpışma Demosu Başlıyor ---")
    print(f"Top 1 Başlangıç: {ball1}")
    print(f"Top 2 Başlangıç: {ball2}")
    
    dt = 0.05
    for i in range(20):
        engine.step(dt)
        print(f"Adım {i+1}:")
        print(f"  Top 1: Pos={ball1.position}, Vel={ball1.velocity}")
        print(f"  Top 2: Pos={ball2.position}, Vel={ball2.velocity}")
        
        # Hızlar yön değiştirdiyse çarpışma oldu demektir
        if ball1.velocity.x < 0 and ball2.velocity.x > 0:
            print(">>> Çarpışma Tespit Edildi ve Çözüldü! <<<")

    print("--- Demo Tamamlandı ---")

if __name__ == "__main__":
    run_collision_demo()
