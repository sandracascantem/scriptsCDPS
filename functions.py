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
def arch(fi, rep1, rep2):
	fin = open('./docker-compose.yaml', 'r')

	with fin as file:
		x= file.read()
	fin.close()

	fin = open('./docker-compose.yaml', 'w')
	with fin as file:
		x= x.replace(rep1, rep2)
		fin.write(x)
	fin.close()
