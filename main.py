import subprocess
import os


pathimg = "src/web/"

dirhome = os.listdir(pathimg)
process = subprocess.Popen(["streamlit", "run", pathimg+dirhome[0]])



