##Largest prime factor
##Problem 3 
##The prime factors of 13195 are 5, 7, 13 and 29.

##What is the largest prime factor of the number 600851475143 ?

def factorizar_nro(nro,primox):
    if nro/primox == 1: return primox
    if nro % primox == 0:
        return factorizar_nro(nro/primox, primox)
    else:
        return factorizar_nro(nro,get_next_prime(primox))

def get_next_primex(lista):
    ultimoPrimo = lista[-1]
    ultimoPrimo = ultimoPrimo + 1
    while(True):
        if es_primo(ultimoPrimo): return ultimoPrimo
        else: ultimoPrimo = ultimoPrimo + 1

def get_next_prime(nro):
    ultimoPrimo = nro + 1
    while(True):
        if es_primo(ultimoPrimo): return ultimoPrimo
        else: ultimoPrimo = ultimoPrimo + 1
            
def es_primo(nro):
    for i in range(2,nro):
        if nro % i == 0:
            return False
    return True

def numeros_primos_de(n):
    rango = int(n/2)
    primos = []
    for i in range(1,rango):
        if n % i == 0:
            primos.append(i)
    return primos

print(get_next_prime(200))
print(factorizar_nro(600851475143,2))
