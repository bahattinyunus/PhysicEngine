# 📖 Teknik Terimler Sözlüğü (Glossary)

Bu doküman, **PhysicEngine** projesinde ve genel fizik simülasyonlarında kullanılan teknik terimlerin Türkçe açıklamalarını içermektedir.

---

### 🟢 A
- **AABB (Axis-Aligned Bounding Box):** Eksenlerle hizalanmış sınırlayıcı kutu. Çarpışma tespiti için kullanılan en basit dikdörtgen formudur. Döndürülemez, sadece x ve y eksenlerine paraleldir.
- **Acceleration (İvme):** Birim zamandaki hız değişimi. $F = m \cdot a$ formülüyle hesaplanır.

### 🔵 C
- **Collision Detection (Çarpışma Tespiti):** İki nesnenin uzayda çakışıp çakışmadığını belirleme süreci.
- **Collision Resolution (Çarpışma Çözümleme):** Çarpışma tespit edildikten sonra nesnelerin hızlarının ve konumlarının fizik kurallarına göre güncellenmesi.

### 🟡 D
- **Delta Time (dt):** İki simülasyon karesi (frame) arasında geçen süre. Simülasyonun gerçek zamanlı akması için kritiktir.
- **Dot Product (Noktasal Çarpım):** İki vektörün birbiri üzerindeki izdüşümünü ve aralarındaki açıyı belirlemek için kullanılan matematiksel işlem.

### 🔴 I
- **Impulse (İtme/İmpuls):** Çok kısa bir süre içinde uygulanan ve hızda ani değişime neden olan kuvvetin integralidir. Çarpışma anındaki hız değişimini hesaplamak için kullanılır.
- **Integration (Entegrasyon):** İvmeden hıza, hızdan konuma geçme işlemi. Projemizde **Semi-implicit Euler** yöntemi kullanılmaktadır.
- **Inverse Mass (Ters Kütle):** $1/mass$ değeridir. Matematiksel işlemlerde bölme işlemini azaltmak ve sonsuz kütleli (statik) nesneleri temsil etmek için kullanılır.

### 🟣 M
- **Manifold:** Çarpışma verilerini (normal, temas noktası, derinlik) tek bir yapıda toplayan veri bloğu.
- **Magnitude (Büyüklük):** Bir vektörün uzunluğu.

### 🟠 P
- **Penetration Depth (İç İçe Geçme Derinliği):** İki nesnenin çarpışma sırasında birbirinin içine ne kadar girdiğini gösteren değer.
- **Positional Correction (Konum Düzeltme):** Nesnelerin kayan noktalı sayıataları nedeniyle birbirinin içinde "hapis kalmasını" (sinking artifact) önlemek için yapılan ufak konum güncellemeleri.

### ⚪ R
- **Restitution (Geri Sekme Katsayısı):** Nesnenin çarpışmadan sonraki "esnekliğini" belirtir. `0` değeri tamamen yapışkan (inelelastik), `1` değeri ise enerjinin korunduğu (mükemmel esnek) çarpışmaları temsil eder.

---
*Geliştirici: Bahattin Yunus Çetin*
