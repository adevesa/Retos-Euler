##Lattice paths
##Problem 15 
##Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
##
##https://projecteuler.net/project/images/p015.gif
##How many such routes are there through a 20×20 grid?

def crear_matriz_binaria(filas,columnas):
    fila = []
    matriz = []
    for i in range(columnas):
        fila.append(0)
    for j in range(filas):
        matriz.append(fila)
    return matriz
    
def ultimo_movimiento(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        for j in range(columnas):
            if es_el_ultimo(matriz,i,j) and matriz[i][j] == 1: return i,j

def es_el_ultimo(matriz,i,j):
    filas = len(matriz)
    columnas = len(matriz[0])

    if i+2 > filas:
        if matriz[i][j+1] == 0: return True
    if j+2 > columnas:
        if matriz[i+1][j] == 0: return True
    if matriz[i][j+1] == 0 and matriz[i+1][j] == 0: return True
    else: return False

def move_right(matriz):
    i,j = ultimo_movimiento(matriz)
    matriz[i][j+1] = 1
    return matriz

def move_down(matriz):
    i,j = ultimo_movimiento(matriz)
    matriz[i+1][j] = 1
    return matriz

matriz_ex = [[1,1,0],[0,1,0],[0,0,0]]
print(move_down(matriz_ex))

