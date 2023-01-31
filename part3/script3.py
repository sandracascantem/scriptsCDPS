#!/usr/bin/python3

import os, sys, subprocess, re
from subprocess import call, run

#Funcion para reemplazar dentro del docker-compose.yaml
def dcompose_ver(fi, version):
	# dictionary to store environment variables based on version
	env_vars = {
		"v1": {"SERVICE_VERSION": "v1", "ENABLE_RATINGS": "false", "STAR_COLOR": "black"},
		"v2": {"SERVICE_VERSION": "v2", "ENABLE_RATINGS": "true", "STAR_COLOR": "black"},
		"v3": {"SERVICE_VERSION": "v3", "ENABLE_RATINGS": "true", "STAR_COLOR": "red"}
	}
	# check if the specified version is valid
	if version not in env_vars:
        	print("Choose a valid version [v1, v2, v3]")
        	return

	# read the contents of the docker-compose.yaml file
	fin = open(fi, "r")
	with fin as file:
        	contents = file.read()
	fin.close()
	
	# split the contents into lines
	lines = contents.split("\n")
	# flag to keep track of the "details" section
	in_details = False
	# updated lines with environment variables for "details" section
	updated_lines = []
	
	for line in lines:
		# check if we're in the "details" section
		if line.startswith("  details:"):
			in_details = True

		# if we're in the "details" section, update environment variables
		if in_details:
			# check if the line starts with "  - SERVICE_VERSION="
			if line.startswith("      - SERVICE_VERSION="):
				# replace the line with the new value from the dictionary
				line = "      - SERVICE_VERSION={}\n".format(env_vars[version]["SERVICE_VERSION"])

			# check if the line starts with "  - ENABLE_RATINGS="
			if line.startswith("      - ENABLE_RATINGS="):
				# replace the line with the new value from the dictionary
				line = "      - ENABLE_RATINGS={}\n".format(env_vars[version]["ENABLE_RATINGS"])

			# check if the line starts with "  - STAR_COLOR="
			if line.startswith("      - STAR_COLOR="):
				# replace the line with the new value from the dictionary
				line = "      - STAR_COLOR={}\n".format(env_vars[version]["STAR_COLOR"])
				
	# add the line to the updated_lines list
	updated_lines.append(line)
	
	# check if we've reached the end of the "details" section
	if line.startswith("    ports:"):
		in_details = False

	# join the updated lines with newline characters
	updated_contents = "\n".join(updated_lines)
	
	# write the updated contents to the docker-compose.yaml file
	fin = open(fi, "w")
	with fin as file:
		file.writelines(updated_contents)
	fin.close()

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
