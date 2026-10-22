import numpy as np
import streamlit as st

def ampliar(imagem, k=10):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Bandeira do Brasil")

bandeira = np.zeros((60, 100, 3), dtype=np.uint8)

bandeira[:] = (0, 156, 59)

for y in range(60):
    largura = int(44 * (1 - abs(y - 29.5) / 25))
    inicio = int(49.5 - largura)
    fim = int(49.5 + largura)
    bandeira[y, inicio:fim] = (255, 223, 0)

for y in range(60):
    for x in range(100):
        if (x - 49.5) ** 2 + (y - 29.5) ** 2 <= 15 ** 2:
            bandeira[y, x] = (0, 39, 118)

st.image(ampliar(bandeira), use_container_width=True)
