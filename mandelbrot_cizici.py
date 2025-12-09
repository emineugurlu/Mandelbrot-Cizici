import numpy as np
import matplotlib.pyplot as plt


MAX_ITERASYON = 500

def fraktal_hesapla_kup(c):
    z= 0 + 0j
    for n in range(MAX_ITERASYON):
        z = z**3 + c 
        if abs(z) > 2.0:
            return n 
    return MAX_ITERASYON


GENISLIK = 800
YUKSEKLIK = 600

REEL_MIN = -1.5
REEL_MAX = 1.5
SANAL_MIN = -1.5
SANAL_MAX = 1.5

resim_dizisi = np.zeros((YUKSEKLIK, GENISLIK))


for x in range(GENISLIK):
    for y in range(YUKSEKLIK):
        
        
        reel_kisim = REEL_MIN + (x / GENISLIK) * (REEL_MAX - REEL_MIN)
        sanal_kisim = SANAL_MIN + (y / YUKSEKLIK) * (SANAL_MAX - SANAL_MIN)
        c =complex(reel_kisim, sanal_kisim)
        
        
        iterasyon_sayisi = fraktal_hesapla_kup(c)
        
        
        resim_dizisi[y, x] = iterasyon_sayisi


plt.imshow(resim_dizisi, cmap='twilight') 
plt.axis('off')
plt.savefig("mandelbrot_ilk_cizim.png", bbox_inches='tight', pad_inches=0)

print("Mandelbrot kümesi çizildi: mandelbrot_ilk_cizim.png")

