#!/usr/bin/python3

import os, sys, subprocess
from subprocess import call

#Funcion arch para reemplazar dentro de un archivo
def arch(fi, rep1, rep2):
	fin = open('./practica_creativa2/bookinfo/src/productpage/' + fi, 'r')

	with fin as file:
		x= file.read()
	fin.close()

	fin = open('./practica_creativa2/bookinfo/src/productpage/' + fi, 'w')
	with fin as file:
		x= x.replace(rep1, rep2)
		fin.write(x)
	fin.close()

#Clonamos la carpeta practica_creativa2 del github
subprocess.run(["git", "clone", "https://github.com/CDPS-ETSIT/practica_creativa2"])
#Cambiamos de directorio (a partir de ahora se trabaja dentro de la carpeta practica_creativa2)
#os.chdir('/home/sandracascantemoran/scriptsCDPS')
