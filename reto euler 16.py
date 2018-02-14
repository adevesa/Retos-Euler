##Power digit sum
##Problem 16 
##215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
##
##What is the sum of the digits of the number 2^1000?

def problema():
    potencia = 2**1000
    str_potencia = str(potencia)
    suma = 0
    for i in str_potencia:
        suma = suma + int(i)
    return suma

print(problema())
