#!/usr/bin/python3

#Funcion arch para reemplazar dentro de un archivo
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
