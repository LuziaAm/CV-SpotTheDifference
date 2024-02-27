import os
from PIL import Image


def get_file():
    s = "/home/luzia-tpv/Documentos/CV-AI/CV-SpotTheDifference/img/"
    file = os.listdir(s)
    namefile = file[0]
    # img = Image.open(s + namefile)
    return namefile