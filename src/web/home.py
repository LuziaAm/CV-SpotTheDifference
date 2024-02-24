import streamlit as st
from PIL import Image


uploaded_files = st.file_uploader("Upload your file here...", accept_multiple_files=True)
try:
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        imagem = Image.open(uploaded_file)
        st.image(imagem)
        st.button("Gerar Jogo")
        imagem.save("/home/luzia-tpv/Documentos/CV-AI/CV-SpotTheDifference/src/img/teste.png")
except NameError:
  print("Variable x is not defined")

