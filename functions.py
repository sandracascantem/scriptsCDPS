#!/usr/bin/python3

#Funcion arch para reemplazar dentro de un archivo de practica_creativa2
def arch(fi, rep1, rep2):
	fin = open('./practica_creativa2/bookinfo/src/productpage/' + fi, 'r')

	with fin as file:
		x= file.read()
	fin.close()

	fin = open('./practica_creativa2/bookinfo/src/productpage/' + fi, 'w')
	with fin as file:
		x= x.replace(rep1, rep2)
		fin.write(x)
	fin.close()

#Funcion arch2 para reemplazar dentro del docker-compose.yaml de part3
def arch2(fi, fila, rep1, rep2):
	fin = open('./docker-compose.yaml', 'r')

	with fin as file:
		in fila:
			x= file.read()
	fin.close()

	fin = open('./docker-compose.yaml', 'w')
	with fin as file:
		in fila:
			x= x.replace(rep1, rep2)
			fin.write(x)
	fin.close()

#Cambia las filas correspondientes a la version de reviews en el docker-compose
def dcompose_vers(filas, antiguo_dato, nuevo_dato):
    contenido = list()
    with open('./docker-compose.yaml', 'r+') as archivo:
        contenido = archivo.readlines()
        for fila in filas:
            columnas = contenido.replace
            columnas[columna] = nuevo_dato
            contenido[fila-1] = ';'.join(columnas)+ '\n'
    with open(ruta, 'w') as archivo:
        archivo.writelines(contenido)
	
#ec
def compose_cambio(archivo, linea, texto):
	contenido = file(archivo).read().splitlines()
	contenido.insert(linea, texto)
	f = file(archivo, "w")
	f.writelines("\n".join(contenido))
