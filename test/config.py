
"""
Añadir directorios al path del proyecto
"""

import sys
import os

dirs = ['src']

for nameDir in dirs:
    path = os.path.join(sys.path[0][:-4], nameDir)
    sys.path.append(path)