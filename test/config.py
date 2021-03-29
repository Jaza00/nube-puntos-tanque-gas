import sys
import os

"""
Añadir directorios al path del proyecto
"""

dirs = ['src']

for nameDir in dirs:
    path = os.path.join(sys.path[0][:-4], nameDir)
    print(path)
    sys.path.append(path)