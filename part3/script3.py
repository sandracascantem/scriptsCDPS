#!/usr/bin/python3

import os, sys, subprocess
from subprocess import call, run

def compose_cambio(archivo, linea, texto):
	contenido = file(archivo).read().splitlines()
	contenido.insert(linea, texto)
	f = file(archivo, "w")
	f.writelines("\n".join(contenido))
 
#Clonamos la carpeta practica_creativa2 del github
run(["git", "clone", "https://github.com/CDPS-ETSIT/practica_creativa2"])

#Copiamos ficheros
run(["cp", "practica_creativa2/bookinfo/src/details/details.rb", "./details/."])
run(["cp", "practica_creativa2/bookinfo/src/details/.DS_Store", "./details/."])
run(["cp", "practica_creativa2/bookinfo/src/ratings/ratings.js", "./ratings/."])
run(["cp", "practica_creativa2/bookinfo/src/ratings/package.json", "./ratings/."])
run(["cp", "practica_creativa2/bookinfo/src/ratings/.DS_Store", "./ratings/."])

#Cambiamos de directorio (a partir de ahora se trabaja dentro de la ruta src/reviews/reviews-wlpcfg)
os.chdir('./practica_creativa2/bookinfo/src/reviews')

#Compilar y empaquetar ficheros necesarios
call(['sudo docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build'], shell=True)

#Seleccionamos la version de review que queremos y modificamos el docker-compose:
version = input("Introduce la versión de reviews deseada (v1, v2, v3): \n")

while version != "v1" or version != "v2" or version != "v3":
  version = input("ERROR: Introduce una versión correcta para reviews (v1, v2, v3) !!!: \n")

if version == "v1":
  exit()
elif version == "v2":
  arch2("./docker-compose-prueba.yaml", 30, "false", "true")
  arch2("./docker-compose-prueba.yaml", 31, "v1", "v2")
  exit()
elif version == "v3":
  arch2("./docker-compose-prueba.yaml", 30, "false", "true")
  arch2("./docker-compose-prueba.yaml", 31, "v1", "v3")
  arch2("./docker-compose-prueba.yaml", 32, "black", "red")
  exit()
