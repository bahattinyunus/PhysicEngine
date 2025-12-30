from src.core.vector import Vector2D
from src.core.body import Body
from src.core.engine import Engine
import time

def run_simulation():
    # Motoru başlat (Standart yerçekimi ile)
    engine = Engine(gravity=Vector2D(0, -9.81)) # Yukarı yönlü pozitif varsayarsak, yerçekimi -9.81

    # Bir nesne oluştur (1kg, 10 metre yükseklik)
    ball = Body(mass=1.0, position=Vector2D(0, 10), velocity=Vector2D(2, 5))
    engine.add_body(ball)

    print("--- Simülasyon Başlıyor ---")
    print(f"Başlangıç Durumu: {ball}")
    
    dt = 0.1 # 100ms zaman adımı
    for i in range(20):
        engine.step(dt)
        print(f"Adım {i+1} (t={round((i+1)*dt, 1)}s): Konum={ball.position}, Hız={ball.velocity}")
        
        # Yere çarptıysa durdur
        if ball.position.y <= 0:
            print("Yere temas gerçekleşti.")
            break

    print("--- Simülasyon Tamamlandı ---")

if __name__ == "__main__":
    run_simulation()
