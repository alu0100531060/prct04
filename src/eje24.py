#!/usr/bin/python
#!encoding: UTF-8
from math import *

a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))
c = float(raw_input('Valor de c: '))
if a != 0:
	x1 = (-b + sqrt(b**2 - 4*(a*c))) / (2 * a)
	x2 = (-b - sqrt(b**2 - 4*(a*c))) / (2 * a)
	print 'Las soluciones de la ecuacion son: x1=%4.3f y x2=%4.3f' % (x1, x2)
else:
	if b != 0:
		x = -c / b
		print 'La solucion de la ecuacion es: x=%4.3f' % x
	else:
		if c != 0:
			print 'La ecuacion no tiene solucion'
		else:
			print 'La ecuacion tiene infinitas soluciones'

# Si a es distinto de 0 entonces se trata de una ecuacion de 2º grado y se resuelve a través de las fórmulas puestas.
# Si a es cero y b distinto de cero, se trata de una ecuación de 1º grado y se calcula como allí se indica.
# Si a y b tienen valor 0 muestra por pantalla que la función tiene infinitas ó ninguna solución en función de si la variable c toma el valor 0 o no.