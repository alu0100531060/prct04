#!/usr/bin/python
#!encoding: UTF-8
from math import sqrt

a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))
c = float(raw_input('Valor de c: '))
if a == 0:
	if b == 0:
		if c == 0:
			print 'La ecuacion tiene infinitas soluciones'
		else:
			print 'La ecuacion no tiene solucion'
	else:
		x = -c / b
		print 'La solucion de la ecuacion es: x=%4.3f' % x
else:
	x1 = (-b + sqrt(b**2 - 4*a*c)) / (2 * a)
	x2 = (-b - sqrt(b**2 - 4*a*c)) / (2 * a)
	print 'Las soluciones de la ecuacion son: x1=%4.3f y x2=%4.3f' % (x1, x2)

# La diferencia con el problema 24 radica en que las condiciones que se solicitan en el problema 24 lo hacen a través de diferencias y en este se hacen a través de igualdadades. 
