import os
from PIL import Image


class Getimg:
    def get_file(self):
        s = "/home/luzia-tpv/Documentos/CV-AI/CV-SpotTheDifference/src/img/"
        file = os.listdir(s)
        namefile = file[0]
        # img = Image.open(s + namefile)
        return namefile