import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")

foto = Image.open("imagens/foto.jpg")
img = np.array(foto)

st.header("4. Tons de cinza")
col1, col2 = st.columns(2)

r = img[:, :, 0].astype(float)
g = img[:, :, 1].astype(float)
b = img[:, :, 2].astype(float)

media = ((r + g + b) / 3).astype(np.uint8)
col1.image(media, caption="Média simples")

peso_r = st.slider("Peso do canal R", 1, 100, 30)
peso_g = st.slider("Peso do canal G", 1, 100, 59)
peso_b = st.slider("Peso do canal B", 1, 100, 11)
peso_total = peso_r + peso_g + peso_b

ponderada = ((peso_r * r + peso_g * g + peso_b * b) / peso_total).astype(np.uint8)
col2.image(ponderada, caption="Média ponderada")

st.header("5. Canais")
canal = st.slider("Canal escolhido: 0 = R, 1 = G, 2 = B", 0, 2, 0)
col1, col2 = st.columns(2)

col1.image(img[:, :, 0], caption="Canal R em tons de cinza")
col1.image(img[:, :, 1], caption="Canal G em tons de cinza")
col1.image(img[:, :, 2], caption="Canal B em tons de cinza")

canal_cor = np.zeros(img.shape, dtype=np.uint8)
canal_cor[:, :, canal] = img[:, :, canal]

if canal == 0:
    nome_canal = "R"
elif canal == 1:
    nome_canal = "G"
else:
    nome_canal = "B"

col2.image(canal_cor, caption=f"Canal {nome_canal} na sua cor")

st.header("8. Negativo")
negativo = 255 - img
col1, col2 = st.columns(2)
col1.image(img, caption="Foto original")
col2.image(negativo, caption="Foto em negativo")

st.header("11. Espelhamento")
horizontal = img[:, ::-1]
vertical = img[::-1, :]
col1, col2 = st.columns(2)
col1.image(img, caption="Foto original")
col2.image(horizontal, caption="Espelhamento horizontal")
col2.image(vertical, caption="Espelhamento vertical")

st.header("20. Pixel art")
passo = st.slider("Passo entre os pixels", 2, 32, 8)
altura, largura = img.shape[0], img.shape[1]
reduzida = img[::passo, ::passo]
pixelada = reduzida.repeat(passo, axis=0).repeat(passo, axis=1)
pixelada = pixelada[:altura, :largura]
col1, col2 = st.columns(2)
col1.image(img, caption="Foto original")
col2.image(pixelada, caption=f"Pixel art - passo {passo}")
