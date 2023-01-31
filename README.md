# Memoria para la práctica creativa 2 CDPS
#Creado por Antonio Ardura Carnicero, Sandra Cascante Morán y Martín Rodríguez Barroso

#Grupo 35

Se puede acceder a los mismos archivos a través de nuestro repositorio de github: https://github.com/sandracascantem/scriptsPC2

-----Part1-----DESPLIEGUE DE LA APLICACIÓN EN MÁQUINA VIRTUAL PESADA-----

La idea es desplegar la aplicación como si fuera un monolito en una máquina virtual pesada en Google Cloud. Para ello, hemos creado el script "script1.py" entregado en el zip, dentro de la carpeta "part1".

Para probarlo, hemos creado una MV en Google Cloud y abierto su consola SSH en un nuevo navegador. Además, hemos instalado git con el comando "sudo apt-get install git" para poder clonar la carpeta con los scripts. A continuación, nos cambiamos al directorio de la carpeta de esta parte (scriptsCDPS/part1).

Ejecutamos el script con el comando "python3 script1.py". Este script:

	-Clona la carpeta practica_creativa2 del github de la asignatura (https://github.com/CDPS-ETSIT/practica_creativa2.git).
  
	-Instala pip en la maquina virtual y se instalan las dependencias de requirements con pip3.
  
	-Crea la variable de entorno "GROUP_NUMBER" que es nuestro número de grupo (35).
  
	-Modifica el productpage.html para cambiar el título de la app por la variable de entorno.
  
	-Pide introducir un puerto en el rango 8980-9080 para cambiarlo en el fichero de la aplicación. 
	Por ello, se ha introducido una regla de FW en Google Cloud donde a los puertos TCP se les ha asignado el rango de puertos mencionado anteriormente. 
	(En caso de introducir un puerto fuera de dicho rango sale del script y no se ejecuta nuestra aplicación monolítica, habría que volver a ejecutar el script introduciendo un puerto correcto).
  
	-Llama a "productpage_monolith.py" (script de la app) con el puerto introducido (correctamente) en el paso anterior.


A continuación, introducimos en el navegador la ip pública de la instancia (MV) con el puerto introducido: http://(ip-publica):(puerto)/productpage obteniendo el resultado esperado.
  
![Captura de pantalla de 2023-01-09 19-08-51](https://user-images.githubusercontent.com/99333138/211384476-570fd7cf-4d89-411f-bf6a-d37cfc534b9b.png)

Como podemos observar, el título de la aplicación es en nuestro caso 35 y la conexión se establece correctamente. Dicha aplicación está compuesta por dos servicios: uno para la página de productos y otro para la descripción de los productos.



-----Part2-----DESPLIEGUE DE UNA APLICACIÓN MONOLÍTICA USANDO DOCKER-----

Ahora se quiere desplegar la misma aplicación monolítica pero usando docker. Para ello, hemos creado el script "script2.py" entregado en el zip, dentro de la carpeta "part2", que automatiza la creación de las imágenes y contenedores docker. Además de, lógicamente, el fichero "Dockerfile", un script que se ejecuta dentro de los contenedores docker (se hace run desde el Dockerfile) llamado "docker.py" y un script "delete.py" que eliminará los contenedores e imágenes creadas de docker, (una vez que ha sido lanzada la aplicación con "script2.py").

Ejecutamos el script con el comando "python3 script2.py". Este script:

	-Construye la imagen de docker "35/product-page".
	-Arranca el contenedor de docker "35-productpage".


La imagen (y por consiguiente el contenedor) se construye según el contenido del "Dockerfile". Este fichero:

	-Contiene la variable de entorno "GROUP_NUMBER" que es nuestro número de grupo (35).
	-Copia y ejecuta el script "docker.py" para la imagen durante su proceso de construcción.
	-Expone el puerto 9080 a través del cual se va a acceder a la aplicación.
	-Ejecuta "productpage_monolith.py" (script de la app) con el puerto 9080 tras haber inicializado el contenedor.


El script "docker.py" mencionado, que se utiliza para crear la imagen del contenedor. Este script:

	-Clona la carpeta practica_creativa2 del github de la asignatura (https://github.com/CDPS-ETSIT/practica_creativa2.git).
	-Instala pip y se instalan las dependencias de requirements con pip3.
	-Extrae la variable de entorno "GROUP_NUMBER" creado en el Dockerfile.
	-Modifica el productpage.html para cambiar el título de la app por la variable de entorno.
	
	
El script "delete.py"

	-Borra el contenedor creado "35-productpage".
	-Borra la imagen creada "35/product-page".
	

A continuación, introducimos en el navegador la ip pública de la instancia (MV) con el puerto introducido: http://(ip-publica):(puerto)/productpage obteniendo el resultado esperado.

<img width="1440" alt="Captura de pantalla 2023-01-31 a las 17 12 58" src="https://user-images.githubusercontent.com/99333138/215816874-f219570c-837b-4cc8-8e82-385e753abe8e.png">

Como podemos observar, el título de la aplicación es en nuestro caso 35 y la conexión se establece correctamente. Dicha aplicación está compuesta por dos servicios: uno para la página de productos y otro para la descripción de los productos.


>> Incluir la línea de comando del despliegue del contenedor en la memoria: nosotros incluimos los comandos que se piden en el "script2.py"

	-La imagen de docker se construye con: "sudo docker build -t 35/product-page .
	-El contenedor de docker se arranca con: "sudo docker run --name 35-productpage -p9080:9080 35/product-page



-----Part3-----SEGMENTACIÓN DE UNA APLICACIÓN MONOLÍTICA EN MICROSERVICIOS UTILIZANDO DOCKER-COMPOSE-----
