##Special Pythagorean triplet
##Problem 9 
##A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
##
##a2 + b2 = c2
##For example, 32 + 42 = 9 + 16 = 25 = 52.
##
##There exists exactly one Pythagorean triplet for which a + b + c = 1000.
##Find the product abc.
from math import sqrt

def valor_pitagorico(a,b):
    return a*a + b*b

def es_entero(c):
    if type(c) == type(1):return True
    else: return False

def es_entero_sqrt(c):
    if int(c) == c: return True
    else: return False

def tripleta_pitagorica(a,b):
    c = sqrt(a*a + b*b)
    if a < b and b < c and es_entero(a) and es_entero(b) and es_entero_sqrt(c):
        return True
    else:
        return False

def suma_de_tripleta(a,b):
    return a + b + sqrt(a*a + b*b)

def problema():
    for a in range(1,1000):
        for b in range(1,1000):
            if tripleta_pitagorica(a,b):
                if suma_de_tripleta(a,b) == 1000: return a * b * sqrt(a*a + b*b)
            b = b + 1
        a = a + 1

print(problema())

