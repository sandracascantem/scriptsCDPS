#!/usr/bin/python3

import os, sys, subprocess
from subprocess import call

#Funcion arch para reemplazar dentro de un archivo de practica_creativa2
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

#Modificamos el fichero requirements.txt
arch('requirements.txt', 'urllib3==1.26.5', 'urllib3')
arch('requirements.txt', 'chardet==3.0.4', 'chardet')
arch('requirements.txt', 'gevent==1.4.0', 'gevent')
arch('requirements.txt', 'greenlet==0.4.15', 'greenlet')
#Instalamos pip sudo apt-get install python-pip
subprocess.run(["apt-get", "install", "python3-pip"])
#Instalamos dependencias de requirements.txt con pip
subprocess.run(["pip3", "install", '-r', './practica_creativa2/bookinfo/src/productpage/requirements.txt'])

#Extraemos la variable de entorno (definida en el Dockerfile) y guardarla aqui
title = os.environ.get('GROUP_NUMBER')

#Modificamos productpage.html para cambiar el titulo de la app por la variable de entorno
arch('templates/productpage.html', 'Simple Bookstore App', title)
