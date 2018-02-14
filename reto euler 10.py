##Summation of primes
##Problem 10 
##The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
##
##Find the sum of all the primes below two million.
from math import sqrt

def es_primo(nro):
    for i in range(2, int(sqrt(nro)+1)):
        if nro % i == 0:
            return False
    return True

def problema(n):
    primos = [2,3]
    conteo = 5
    while conteo <= n:
        if es_primo(conteo):
            primos.append(conteo)
        conteo = conteo + 1
    return sum(primos)

print(problema(2000000))
