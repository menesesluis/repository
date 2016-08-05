# -*- coding: utf-8 -*-
print "Mi equipo es:\nRosas Colula Luis Angel\nMiguel Angel Vazquez (Alias: Samanta)\nAna\nCharli\nMeneses "
l = raw_input("ingresa el tamaño de la cadena:\n ")
arreglo = []
for i in range(0, int(l)):
	arreglo.append(raw_input("ingresa el elemento: "))
print "La cadena es:\n"
print arreglo
print "Tam",len(arreglo)
inicio = 0
finalizar = 2
actual = inicio
fin =False
contador = 0
while (fin==False):
	if(contador > len(arreglo)-1):
		fin=True
		break
	if(actual==0):
		if(arreglo[contador]=="a"):
			actual=0
		if(arreglo[contador]=="b"):
			actual=1
		contador+= 1
		continue
	if(actual==1):
		if(arreglo[contador]=="a"):
			actual=2
		if(arreglo[contador]=="b"):
			actual=3
		contador+= 1
		continue
	if(actual==2):
		if(arreglo[contador]=="a"):
			actual=4
		if(arreglo[contador]=="b"):
			actual=2
		contador+= 1
		continue
if(actual==finalizar):
	print "la cadena es aceptada por el automata"
else:
	print "la cadena no es aceptada por el automata"
print fin
print inicio
print finalizar
print actual
print contador
