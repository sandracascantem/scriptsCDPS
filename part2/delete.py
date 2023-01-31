#!/usr/bin/python3

import os, sys, subprocess, yaml
from subprocess import call, run

#Borra el contenedor creado
subprocess.run(["sudo", "docker", "rm", "35-productpage"])
#Borra la imagen creada
subprocess.run(["sudo", "docker", "rmi", "35/product-page"])
