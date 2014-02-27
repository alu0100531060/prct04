#!/usr/bin/python
#!encoding: UTF-8

a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))

if a != 0:
	x = -b/a
	print 'Solucion: ', x
if a = 0:
	print 'La ecuación no tiene solución.'

# El error radica en que al principio pedimos un valor para la variable a
# y luego obligamos a que a tenga el valor 0.

# LA propuesta de solución está en otro archivo