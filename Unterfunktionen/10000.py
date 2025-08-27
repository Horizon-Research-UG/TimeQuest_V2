import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from werkzeug.abstand import abstand

abstand()
if input("Husslen oder speichern? (h/s)") == "h":
    print("Husslen...")
else:
    print("Speichern...")
    input("Was möchtest du speichern?")