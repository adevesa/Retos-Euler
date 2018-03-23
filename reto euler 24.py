from itertools import permutations

listado = []
for p in permutations([0,1,2,3,4,5,6,7,8,9],10):
    listado.append(p)

sorted(listado)
print(listado[999999])