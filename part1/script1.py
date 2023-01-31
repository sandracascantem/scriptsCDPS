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
subprocess.run(["sudo", "apt-get", "install", "python3-pip"])
#Instalamos dependencias de requirements.txt con pip
subprocess.run(["pip3", "install", '-r', './practica_creativa2/bookinfo/src/productpage/requirements.txt'])

#Creamos la variable de entorno (con nuestro num de grupo, 35)
os.environ['GROUP_NUMBER']= "35"
#Extraemos la variable de entorno y guardarla aqui
title = os.environ.get('GROUP_NUMBER')

#Modificamos productpage.html para cambiar el titulo de la app por la variable de entorno
arch('templates/productpage.html', 'Simple Bookstore App', title)

#Modificamos el script productpage_monolith.py para cambiar el puerto por otro introducido
puerto = input("Introduce un puerto entre 8980 y 9080: \n")
if int(puerto) < 8980 or int(puerto) > 9080:
	print("ERROR: no se ha seleccionado un puerto valido (entre 8980 y 9080) !!!\n")
	exit()
else:
	arch('productpage_monolith.py', '9080', puerto)

#Llamamos a productpage_monolith.py para crear la aplicacion (como si fuese un monolito)
subprocess.run(["python3", "./practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", puerto])
