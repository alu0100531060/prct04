#!/usr/bin/python
#!encoding: UTF-8

def es_perfecto(n):
	sumatorio = 0
	for i in range(1,n):
		if n % i == 0:
			sumatorio += i
	return sumatorio == n


def tabla_perfectos(m):
	for i in range(1, m+1):
		if es_perfecto(i):
			print i, 'es perfecto'

x = int( raw_input('Introduzca el numero de numeros a calcular si es perfecto o no: '))
tabla_perfectos(x)

#Para este ejercicio, se debe hacer uso de la funcion del ejercicio anterior (eje41.py)
