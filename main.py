import subprocess
import os
from src.core.getfile import get_file

pathimg = "src/web/"
nameimg = get_file()
print(nameimg)
dirhome = os.listdir(pathimg)
process = subprocess.Popen(["streamlit", "run", pathimg+dirhome[0]])



