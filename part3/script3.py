#!/usr/bin/python3

import os, sys, subprocess
from subprocess import call

#Clonamos la carpeta practica_creativa2 del github
subprocess.run(["git", "clone", "https://github.com/CDPS-ETSIT/practica_creativa2"])

#Cambiamos de directorio (a partir de ahora se trabaja dentro de la ruta src/reviews/reviews-wlpcfg)
os.chdir('./practica_creativa2/bookinfo/src/reviews/reviews-wlpcfg')

#compilar y empaquetar ficheros necesarios
call(["docker run --rm -u root -v " + r' " ' + "$(pwd)" + r' " ' + ":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build"], shell=True)

