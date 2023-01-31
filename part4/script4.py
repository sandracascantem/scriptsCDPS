#!/usr/bin/python3

import os, sys, subprocess, yaml
from subprocess import call, run

#Seleccionamos la version de review que queremos
version = input("Introduce la versión de reviews deseada (v1, v2 o v3): \n")

if version == "v1" or version == "v2" or version == "v3":
    #Construimos los servicios de kubernetes
    subprocess.run(["kubectl", "apply", "-f", "productPage/productpage.yaml"])
    subprocess.run(["kubectl", "apply", "-f", "details/details.yaml"])
    subprocess.run(["kubectl", "apply", "-f", "ratings/ratings.yaml"])
    subprocess.run(["kubectl", "apply", "-f", "reviews/reviews-svc.yaml"])
    if version == "v1":
      subprocess.run(["kubectl", "apply", "-f", "reviews/reviews-v1-deployment.yaml"])
    if version == "v2":
      subprocess.run(["kubectl", "apply", "-f", "reviews/reviews-v2-deployment.yaml"])
    if version == "v3":
      subprocess.run(["kubectl", "apply", "-f", "reviews/reviews-v3-deployment.yaml"])
else:
    print("ERROR: se ha introducido una version no valida (v1, v2 o v3) !!!\n")
    exit()
  
