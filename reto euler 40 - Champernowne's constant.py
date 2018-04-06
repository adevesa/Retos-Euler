decimales = ""
for x in range(1,1000000):
    decimales += str(x)

def get_n(n,string):
    return string[n-1:n:]

def problema():
    resultado = 1
    for i in range(7):
        multiplicado = 10 ** i
        resultado *= int(get_n(multiplicado,decimales))
    
    return resultado

print(problema())

