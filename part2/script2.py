#!/usr/bin/python3

import os, sys, subprocess
from subprocess import call

#Construimos la imagen de docker 
subprocess.run(["sudo", "docker" ,"build", "-t", "35/product-page", "."])
#Arrancamos el contenedor de docker
subprocess.run(["sudo", "docker", "run", "--name", "35-productpage","-p9080:9080","35/product-page"])
