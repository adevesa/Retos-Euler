'''

Number spiral diagonals
Problem 28 
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

'''
impares = [x for x in range(1,1002) if x % 2 == 1]
pares = [x for x in range(1,1002) if x % 2 == 0]

cuadrados = list(map(lambda x: x**2, impares))

diagonales = [1]

index_cuadrado = 0
index_par = 0
index_range = 0
pivote = 1

while(index_cuadrado < len(cuadrados) -1 ):
    
    for o in range(4):
        pivote += pares[index_par]
        diagonales.append(pivote)

    index_par += 1
    index_cuadrado += 1

print(sum(diagonales))
    

    



    

    






