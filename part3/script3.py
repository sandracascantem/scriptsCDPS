#!/usr/bin/python3

import os, sys, subprocess, yaml
from subprocess import call, run

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

    # load the yaml file
    with open(fi, "r") as stream:
        data = yaml.safe_load(stream)

    # update the environment variables of the reviews service
    data["services"]["reviews"]["environment"] = env_vars[version]

    # write the updated yaml file
    with open(fi, "w") as stream:
        yaml.dump(data, stream, default_flow_style=False)

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
