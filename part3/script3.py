#!/usr/bin/python3

import os, sys, subprocess, re
from subprocess import call, run

#Funcion para reemplazar dentro del docker-compose.yaml
def dcompose_ver(fin, version):
	options = {
		"v1": {"SERVICE_VERSION": "v1", "ENABLE_RATINGS": "false", "STAR_COLOR": "black"},
		"v2": {"SERVICE_VERSION": "v2", "ENABLE_RATINGS": "true", "STAR_COLOR": "black"},
		"v3": {"SERVICE_VERSION": "v3", "ENABLE_RATINGS": "true", "STAR_COLOR": "red"}
	}
	
	if version not in options:
		print("No se ha seleccionado una versión válida para reviews (v1, v2, v3)\n")
		exit()
	
	with open(fin, "r") as f:
        	lines = f.readlines()

	new_lines = []
    	for line in lines:
		if "SERVICE_VERSION" in line:
			line = re.sub(r"SERVICE_VERSION=\w+", f"SERVICE_VERSION={options[version]['SERVICE_VERSION']}", line)
		if "ENABLE_RATINGS" in line:
			line = re.sub(r"ENABLE_RATINGS=\w+", f"ENABLE_RATINGS={options[version]['ENABLE_RATINGS']}", line)
		if "STAR_COLOR" in line:
			line = re.sub(r"STAR_COLOR=\w+", f"STAR_COLOR={options[version]['STAR_COLOR']}", line)
		new_lines.append(line)

	with open(fin, "w") as f:
        	f.writelines(new_lines)
		
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

#Cambiamos de directorio (a partir de ahora se trabaja dentro de la ruta src/reviews/reviews-wlpcfg)
#os.chdir('./../../../../practica_creativa2/bookinfo/src/reviews')

#Seleccionamos la version de review que queremos y modificamos el docker-compose:
version = input("Introduce la versión de reviews deseada (v1, v2, v3): \n")
dcompose_ver('./../../../../docker-compose-prueba.yaml', str(version))
