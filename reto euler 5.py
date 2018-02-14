##Smallest multiple
##Problem 5 
##2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

##What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def problema2():
    producto = 1
    for i in todos_los_primos_de(20):
        producto = producto * i
    return producto

def problema():
    jejox = problema2()
    while(True):
        for i in range(1,21):
            if jejox % i != 0:
                jejox = jejox + 1
                break
            if i == 20:
                return jejox

def problema2():
    jejox = 1
    while(True):
        for i in range(1,11):
            if jejox % i != 0:
                jejox = jejox + 1
                break
            if i == 10:
                return jejox

def todos_los_primos_de(rango):
    primos = []
    for i in range(2,rango):
        if es_primo(i): primos.append(i)
    return primos

def es_primo(nro):
    for i in range(2,nro):
        if nro % i == 0:
            return False
    return True
        
        

print(problema())
            
