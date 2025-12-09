import numpy as np
import matplotlib.pyplot as plt


MAX_ITERASYON = 500

def mandelbrot_hesapla(c):
    z = 0 + 0j
    for n in range(MAX_ITERASYON):
        z = z**2 + c 
        if abs(z) > 2.0:
            return n 
    return MAX_ITERASYON


GENISLIK = 800
YUKSEKLIK = 600

REEL_MIN = -0.8
REEL_MAX = -0.7
SANAL_MIN = 0.1
SANAL_MAX = 0.2

resim_dizisi = np.zeros((YUKSEKLIK, GENISLIK))


for x in range(GENISLIK):
    for y in range(YUKSEKLIK):
        
        
        reel_kisim = REEL_MIN + (x / GENISLIK) * (REEL_MAX - REEL_MIN)
        sanal_kisim = SANAL_MIN + (y / YUKSEKLIK) * (SANAL_MAX - SANAL_MIN)
        c = complex(reel_kisim, sanal_kisim)
        
        
        iterasyon_sayisi = mandelbrot_hesapla(c)
        
        
        resim_dizisi[y, x] = iterasyon_sayisi


plt.imshow(resim_dizisi, cmap='twilight') 
plt.axis('off')
plt.savefig("mandelbrot_ilk_cizim.png", bbox_inches='tight', pad_inches=0)

print("Mandelbrot kümesi çizildi: mandelbrot_ilk_cizim.png")

