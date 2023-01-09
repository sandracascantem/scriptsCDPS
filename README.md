# Memoria para la práctica creativa 2 CDPS
#Creado por Antonio Ardura Carnicero, Sandra Cascante Morán y Martín Rodríguez Barroso

#Grupo 35

-----DESPLIEGUE DE LA APLICACION EN MAQUINA VIRTUAL PESADA-----

La idea es desplegar la aplicación como si fuera un monolito en una máquina virtual pesada en Google Cloud. Para ello, hemos creado el script "script1.py" entregado en el zip. También lo hemos subido a nuestro repositorio de github: https://github.com/sandracascantem/scriptsCDPS

Para probarlo, hemos creado una MV en Google Cloud y abierto su consola SSH en un nuevo navegador. Además, hemos instalado git con el comando "sudo apt-get install git" para poder clonar la carpeta con los scripts. A continuación nos cambiamos al directorio de dicha carpeta (scriptsCDPS).

Llamamos al script con el comando "python3 script1.py". Este script:

	-Clona la carpeta practica_creativa2 del github de la asignatura.
  
	-Instala pip en la maquina virtual y se instalan las dependencias de requirements con pip3.
  
	-Crea la variable de entorno "GROUP_NUMBER" que es nuestro numero de grupo (35).
  
	-Modifica el productpage.html para cambiar el titulo de la app por la variable de entorno.
  
	-Pide introducir un puerto en el rango 8980-9080 para cambiarlo en el fichero. Esto se debe a una regla del FW en Google Cloud donde a los puertos TCP se les ha asignado el rango de puertos mencionado anteriormente.
  
	-Llama a "productpage_monolith.py" con el puerto introducido en el paso anterior.


A continuación probamos a introducir en el navegador la ip pública de la MV con el puerto introducido (http://<ip-publica>:<puerto>/productpage) obteniendo el resultado esperado.
  
![Captura de pantalla de 2023-01-09 19-08-51](https://user-images.githubusercontent.com/99333138/211384476-570fd7cf-4d89-411f-bf6a-d37cfc534b9b.png)

Como podemos observar, el título de la aplicación es en nuestro caso 35 y la conexión se establece correctamente.
