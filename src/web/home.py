import streamlit as st
import os
from PIL import Image

def get_file():
    s = "/home/luzia-tpv/Documentos/CV-AI/CV-SpotTheDifference/img/"
    file = os.listdir(s)
    namefile = file[0]
    # img = Image.open(s + namefile)
    return namefile

uploaded_files = st.file_uploader("Upload your file here...", accept_multiple_files=True)
print(uploaded_files)
try:
  for uploaded_file in uploaded_files:
      bytes_data = uploaded_file.read()
      imagem = Image.open(uploaded_file)
      # st.image(imagem)
      imagem.save("/home/luzia-tpv/Documentos/CV-AI/CV-SpotTheDifference/img/teste.png")
except NameError:
  print("Variable x is not defined")

namefile = get_file()

withfile =  len(uploaded_files)

if withfile > 0:
  button_gerarjogo = st.button("Gerar Jogo")

  if button_gerarjogo is True:
    col1, col2 = st.columns([3,2])
    with col1:
      st.header("A cat")
      st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
      st.header("A dog")
      st.image("https://static.streamlit.io/examples/dog.jpg")  