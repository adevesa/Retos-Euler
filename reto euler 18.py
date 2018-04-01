##Maximum path sum I
##Problem 18 
##By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
##
##3
##7 4
##2 4 6
##8 5 9 3
##
##That is, 3 + 7 + 4 + 9 = 23.
##
##Find the maximum total from top to bottom of the triangle below:
##
##75
##95 64
##17 47 82
##18 35 87 10
##20 04 82 47 65
##19 01 23 75 03 34
##88 02 77 73 07 63 67
##99 65 04 28 06 16 70 92
##41 41 26 56 83 40 80 70 33
##41 48 72 33 47 32 37 16 94 29
##53 71 44 65 25 43 91 52 97 51 14
##70 11 33 28 77 73 17 78 39 68 17 57
##91 71 52 38 17 14 91 43 58 50 27 29 48
##63 66 04 68 89 53 67 30 73 16 69 87 40 31
##04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
##
##NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

ARBOL_CRUDO = [[75],[95,64],[17,47,82],[18,35,87,10],[20,4,82,47,65],[19,1,23,75,3,34],[88,2,77,73,7,63,67],[99,65,4,28,6,16,70,92],[41,41,26,56,83,40,80,70,33],[41,48,72,33,47,32,37,16,94,29],[53,71,44,65,25,43,91,52,97,51,14],[70,11,33,28,77,73,17,78,39,68,17,57],[91,71,52,38,17,14,91,43,58,50,27,29,48],[63,66,4,68,89,53,67,30,73,16,69,87,40,31],[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]

def armar_arbol():
    pass

def lista_nivel(Lista):
    return len(Lista) - 1
                
class arbol:
    
    def __init__(self, V):
        self.valor = V
        self.padre = None
        self.nivel = 0
        self.hijo_izq = None
        self.hijo_der = None

    def __add__(self,other):
        if self.sin_hijo_izquierdo():
            self.asignar_hijo_izquierdo(other)
        elif self.sin_hijo_derecho():
            self.asignar_hijo_derecho(other)
        return self

    def llenar_triangulo(self,Lista):
        arboles = self.traer_hijos_de_nivel(lista_nivel(Lista))
        arboles = list(arboles)
        arboles[0] = arboles[0] + arbol(Lista.pop(0))
        ult = len(arboles) - 1
        ultL = len(Lista) - 1
        arboles[ult] = arboles[ult] + arbol(Lista.pop(ultL))
        i = 0
        for arb in Lista:
            arbolito = arbol(arb)
            arboles[i] = arboles[i] + arbolito
            if i+2 > len(arboles): arboles[i+1] = arboles[i+1] + arbolito
            i += 1
        return self

    def traer_hijos_de_nivel(self,nivel, hijos = set([])):
        if not self.sin_hijo_izquierdo():
            if self.hijo_izq.nivel == nivel: 
                hijos.add(self.hijo_izq)
            hijos = self.hijo_izq.traer_hijos_de_nivel(nivel,hijos)

        if not self.sin_hijo_derecho():
            if self.hijo_der.nivel == nivel: 
                hijos.add(self.hijo_der)
            hijos = self.hijo_der.traer_hijos_de_nivel(nivel,hijos)

        return hijos

    def esta_lleno(self):
        if self.hijo_izq != None and self.hijo_der != None: return True
        else: return False

    def sin_hijo_izquierdo(self):
        return self.hijo_izq == None

    def sin_hijo_derecho(self):
        return self.hijo_der == None

    def asignar_hijo_izquierdo(self,Arbol):
        if self.sin_hijo_izquierdo():
            self.hijo_izq = Arbol
            Arbol.padre = self
            Arbol.nivel = self.nivel + 1

    def __str1__(self):
        print("Yo soy el arbol con valor: " + str(self.valor))
        print("Soy del nivel: " + str(self.nivel))
        if self.padre == None: print("Soy Raíz")
        if self.sin_hijo_izquierdo() and self.sin_hijo_derecho(): pass
        else:
            print("Mis hijos son: ")
            if self.hijo_izq != None: print(self.hijo_izq)
            if self.hijo_der != None: print(self.hijo_der)
        return ""

    def __str__(self):
        print("Yo soy el arbol con valor: " + str(self.valor))
        print("Soy del nivel: " + str(self.nivel))
        return ""

    def __lt__(self,other):
        if self.nivel < other.nivel:
            return True
        if self.nivel == other.nivel:
            return self.valor < other.valor

    def __gt__(self,other):
        if self.nivel > other.nivel:
            return True
        if self.nivel == other.nivel:
            return self.valor > other.valor

    def asignar_hijo_derecho(self,Arbol):
        if self.sin_hijo_derecho():
            self.hijo_der = Arbol
            Arbol.padre = self
            Arbol.nivel = self.nivel + 1

## Tests:

# arb1 = arbol(1)
# arb2 = arbol(2)
# arb3 = arbol(3)
# arb4 = arbol(4)
# arb5 = arbol(5)
# arb6 = arbol(6)
# arb7 = arbol(7)
# arb8 = arbol(8)
# arb9 = arbol(9)
# arb10 = arbol(10)

# arb1 = arb1 + arb2
# arb1 = arb1 + arb3
# arb2 = arb2 + arb4
# arb2 = arb2 + arb5
# arb3 = arb3 + arb5
# arb3 = arb3 + arb6
# arb4 = arb4 + arb7
# arb4 = arb4 + arb8
# arb5 = arb5 + arb8
# arb5 = arb5 + arb9
# arb6 = arb6 + arb9
# arb6 = arb6 + arb10
# print(arb1.padre)
# print(arb1.hijo_izq.valor)
# print(arb1.hijo_der.valor)
# print(arb2.padre.valor)
# print(arb3.padre.valor)
# print(arb4.valor)
# print(arb4.nivel)
# print(arb1)
# ls = sorted(arb1.traer_hijos_de_nivel(2))
# for i in ls:
#     print(i)

arb1 = arbol(1)
arb2 = arbol(2)
arb3 = arbol(3)
arb1 = arb1 + arb2
arb1 = arb1 + arb3
arb1 = arb1.llenar_triangulo([4,5,6])

print(arb1.__str1__())





