#Carlos Sanchez Paz
#Luis Antonio Meneses Lopez
#Ana Paola Toxcoyoa Cruz


print "Ingrese una cadena"
cadena = raw_input()
print "A0 = E"
print "A1 = "+cadena
A2 = ""
for i in range(len(cadena)):
        for j in range(len(cadena)):
                A2 =A2+ cadena[i]+cadena[j]+","
print "A2 = "+A2
A3 = ""
for i in range(len(cadena)):
        for j in range(len(cadena)):
                for k in range(len(cadena)):
                        A3 =A3+ cadena[i]+cadena[j]+cadena[k]+","
print "A3 = "+A3
A4 = ""
for i in range(len(cadena)):
        for j in range(len(cadena)):
                for k in range(len(cadena)):
                        for l in range(len(cadena)):
                                A4 =A4+ cadena[i]+cadena[j]+cadena[k]+cadena[l]+","
print "A4 = "+A4


