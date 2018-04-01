##Lattice paths
##Problem 15 
##Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
##
##https://projecteuler.net/project/images/p015.gif
##How many such routes are there through a 20×20 grid?

def crear_listas_con_todas_posiblidades():
    inicial = "0" * 40

    inicial = []
    lista.append(inicial)

    final = "1" * 40

    pivote = 39

    iterado = inicial

    while iterado != final:
        
        if iterado[pivote] == "1" and anteriores_unos(iterado,pivote) == True:
            pivote = pivote - 1
            iterado = anteriores_todo_cero(iterado,pivote)
        else: pass

def anteriores_unos(iterado,pivote):

    substr = iterado[pivote+1::]

    for i in substr:
        if i == "1": continue
        else: return False
    return True

def anteriores_todo_cero(iterado,pivote):

    substr = iterado[pivote+1::]
    substr2 = iterado[:pivote:]

    substr2 = substr2 + "1"

    new = ""

    for i in substr:
        new = new + "0"

    return substr2 + new

''' Tests '''

print(anteriores_unos("1111000",3))

print(anteriores_unos("0000111",3))

print(anteriores_todo_cero("0000111",3))
