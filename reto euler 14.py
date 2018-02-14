##Longest Collatz sequence
##Problem 14 
##The following iterative sequence is defined for the set of positive integers:
##
##n → n/2 (n is even)
##n → 3n + 1 (n is odd)
##
##Using the rule above and starting with 13, we generate the following sequence:
##
##13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
##It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
##
##Which starting number, under one million, produces the longest chain?
##
##NOTE: Once the chain starts the terms are allowed to go above one million.

def operacion(n):
    if n%2 == 0:
        return n/2
    else: return (3*n+1)

def cantidad_de_operaciones(n):
    cant = 1
    while n != 1:
        n = operacion(n)
        cant = cant + 1
    return cant

def problema():
    maximo = 0
    n_maximo = 0
    for i in range(1,1000000):
        cant = cantidad_de_operaciones(i)
        if cant > maximo:
            maximo = cant
            n_maximo = i
    return n_maximo

print(problema())
##Solución alternativa. Muy buena.
##def collatz(n,mem):
##    if n in mem.keys():
##        return mem[n]
##    elif n%2 == 0:
##        return collatz(n/2,mem)+1
##    else:
##        return collatz(3*n+1,mem)+1
##
##Lim = 1000000
##lenSeq = {1:1}
##for i in range(1,Lim+1):
##    lenSeq[i] = collatz(i,lenSeq)
##    print(lenSeq)
##print(max(lenSeq, key=lenSeq.get))
