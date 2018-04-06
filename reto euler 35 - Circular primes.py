'''
Circular primes
Problem 35 
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

from math import sqrt
from itertools import permutations

dic_primes = {
    2: True,
    3: True,
}
def es_primo(nro):
    if dic_primes.get(nro) == None:
        if nro < 0: 
            dic_primes.update({nro:False})
            return False
        for i in range(2, int(sqrt(nro)+1)):
            if nro % i == 0:
                dic_primes.update({nro:False})
                return False
        dic_primes.update({nro:True})
        return True
    else: return dic_primes[nro]

primes_numbers = [prime for prime in range(2,1000000) if es_primo(prime)]

def agregar_al_final(string):
    principio = string[0:1:]
    fin = string[1::]

    return fin + principio

def numero_str(num):
    return str(num)

def circular_nums(num):
    numero = numero_str(num)

    n = 0
    length = len(numero)
    lista = []

    while n < length:
        numero = agregar_al_final(numero)
        lista.append(int(numero))
        n += 1
    return lista

def is_circular_number(number):
    for cn in circular_nums(number):
        if not es_primo(cn): return False
    return True

circular_numbers = [x for x in primes_numbers if  is_circular_number(x)]

circular_numbers = sorted(set(circular_numbers))

print(circular_numbers)
print(len(circular_numbers))


