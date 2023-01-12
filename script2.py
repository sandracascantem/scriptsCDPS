#!/usr/bin/python3

import os, sys, subprocess, script0
from subprocess import call
from script0 import arch

#Llamamos al script0 (comandos comunes pc2)
subprocess.run(["python3", "./script0.py"])

#Instalamos entorno docker
subprocess.run(["sudo", "apt", "update"])
subprocess.run(["sudo", "apt", "install", "docker.io"])
subprocess.run(["sudo", "apt", "install", "docker-compose"])

#Creamos Dockerfile
doc = open("./Dockerfile", "w")
doc.write("FROM python:3.7\n")
doc.write("#Clonamos repositorio pc2\nRUN git clone https://github.com/CDPS-ETSIT/practica_creativa2\n")
doc.write("#Variable entorno al contenedor\nENV GROUP_NUMBER '35'\n")
doc.write("#Abrimos el puerto 9080\nEXPOSE 9080\n")
doc.write("#Lanza la aplicacion\nCMD ['python3', './practica_creativa2/bookinfo/src/productpage/productpage_monolith.py', '9080']\n")

#Creamos imagen
subprocess.run(["sudo", "docker", "build", "-t", "35/product-page", "."])

#print(GROUP_NUMBER)
#Modificamos productpage.html para cambiar el titulo de la app por la variable de entorno
#arch('templates/productpage.html', 'Simple Bookstore App', GROUP_NUMBER)

