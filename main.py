import os
import distutils.util
     
cur_dir = os.path.realpath(os.path.dirname(__file__))
fichier = os.path.join(cur_dir, "variable.txt")
     
with open(fichier, "r") as f:
        variable = f.read()
     
vraie_variable = bool(distutils.util.strtobool(variable))
if vraie_variable:
        print("La variable est un boolean True")