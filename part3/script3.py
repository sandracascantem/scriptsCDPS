#!/usr/bin/python3

import os, sys, subprocess
from subprocess import call, run

#Funcion arch2 para reemplazar dentro del docker-compose.yaml de part3
def arch2(arch, version):
	with open(arch, "r") as f:
		contenido = f.readlines()
		for line in contenido:
			#['+' if i > 5 else '-' for i in range(1, 11)]
			if version == "v1":
				service_version = ['\t- SERVICE_VERSION=v1\n' if "SERVICE_VERSION" in line else line for line in contenido]
				enable_ratings = ['\t- ENABLE_RATINGS=true\n' if "ENABLE_RATINGS" in line else line for line in lines_version]
				star_color = ['\t- STAR_COLOR=black\n' if "STAR_COLOR" in line else line for line in lines_ratings]
			elif version == "v2":
				service_version = ['\t- SERVICE_VERSION=v2\n' if "SERVICE_VERSION" in line else line for line in lines]
				enable_ratings = ['\t- ENABLE_RATINGS=true\n' if "ENABLE_RATINGS" in line else line for line in lines_version]
				star_color = ['\t- STAR_COLOR=black\n' if "STAR_COLOR" in line else line for line in lines_ratings]
			elif version == "v3":
				service_version = ['\t- SERVICE_VERSION=v3\n' if "SERVICE_VERSION" in line else line for line in lines]
				enable_ratings = ['\t- ENABLE_RATINGS=true\n' if "ENABLE_RATINGS" in line else line for line in lines_version]
				star_color = ['\t- STAR_COLOR=red\n' if "STAR_COLOR" in line else line for line in lines_ratings]
			else:
				print("No se ha seleccionado una versi´pn correcta de reviews (v1, v2, v3)")
				exit()
	with open("docker-compose.yml", "w") as f:
		f.writelines(star_color)
 
def service_version(arch, version):
	with open(arch, 'r') as fin:
		lines =fin.readlines()
		for line in lines:
			if "SERVICE_VERSION" in line
				
		
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

if str(version) == 'v1':
	exit()
elif str(version) == 'v2':
	arch2("./docker-compose-prueba.yaml", 30, "false", "true")
	arch2("./docker-compose-prueba.yaml", 31, "v1", "v2")
	exit()
elif str(version) == 'v3':
	arch2("./docker-compose-prueba.yaml", 30, "false", "true")
	arch2("./docker-compose-prueba.yaml", 31, "v1", "v3")  
	arch2("./docker-compose-prueba.yaml", 32, "black", "red")
	exit()
else:
	print("ERROR: no se ha seleccionado una versión correcta para reviews (v1, v2, v3)")
	exit()
