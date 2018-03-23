'''
Quadratic primes
Problem 27 
Euler discovered the remarkable quadratic formula:

n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
'''
from math import sqrt

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


def how_many_primes_do(a,b,n):
    cont_primes = 0
    for x in range(n+1):
        f = x**2 + a*x + b
        if es_primo(f): cont_primes +=1
        else: break
    return  cont_primes

cont_max = 0
a_max = 0
b_max = 0
for a in range(-1000,1001):
    for b in range(-1000,1001):
        primes = how_many_primes_do(a,b,10000000)
        if primes > cont_max:
            cont_max = primes
            a_max = a
            b_max = b

#print(how_many_primes_do(1000,1000,1000))
print(cont_max,a_max,b_max)


