##10001st prime
##Problem 7 
##By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

##What is the 10 001st prime number?

def es_primo(nro):
    for i in range(2, int(nro/2) + 1):
        if nro % i == 0:
            return False
    return True

def n_nros_primos(n):
    primos = [2]
    conteo = 3
    while len(primos) != n:
        if es_primo(conteo):
            primos.append(conteo)
        conteo = conteo + 2
    return primos[-1]

print(n_nros_primos(10001))
        
