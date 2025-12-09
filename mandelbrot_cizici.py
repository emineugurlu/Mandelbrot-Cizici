import numpy as np
import matplotlib.pyplot as plt

# --- 1. FONKSİYON VE AYARLAR ---
MAX_ITERASYON = 100 

def mandelbrot_hesapla(c):
    z = 0 + 0j
    for n in range(MAX_ITERASYON):
        z = z**2 + c 
        if abs(z) > 2.0:
            return n 
    return MAX_ITERASYON

# --- 2. RESİM VE DÜZLEM AYARLARI ---
GENISLIK = 800
YUKSEKLIK = 600

REEL_MIN = -2.0
REEL_MAX = 1.0
SANAL_MIN = -1.0
SANAL_MAX = 1.0

# Dizi oluşturma
resim_dizisi = np.zeros((YUKSEKLIK, GENISLIK))

# --- 3. HESAPLAMA DÖNGÜSÜ ---
for x in range(GENISLIK):
    for y in range(YUKSEKLIK):
        
        # Koordinat Eşleme
        reel_kisim = REEL_MIN + (x / GENISLIK) * (REEL_MAX - REEL_MIN)
        sanal_kisim = SANAL_MIN + (y / YUKSEKLIK) * (SANAL_MAX - SANAL_MIN)
        c = complex(reel_kisim, sanal_kisim)
        
        # Hesaplama
        iterasyon_sayisi = mandelbrot_hesapla(c)
        
        # Diziye Kaydetme
        resim_dizisi[y, x] = iterasyon_sayisi

# --- 4. GÖRSELLEŞTİRME KISMI (Matplotlib) ---
# cmap='hot' yerine farklı bir renk haritası kullanacağız.
plt.imshow(resim_dizisi, cmap='twilight') 
plt.axis('off')
plt.savefig("mandelbrot_ilk_cizim.png", bbox_inches='tight', pad_inches=0)

print("Mandelbrot kümesi çizildi: mandelbrot_ilk_cizim.png")

# plt.show()