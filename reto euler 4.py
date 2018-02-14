##Largest palindrome product
##Problem 4 
##A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

##Find the largest palindrome made from the product of two 3-digit numbers.

def nro_palindromo(nro):
    stringeado = str(nro)
    if stringeado == stringeado[::-1]: return True
    else: return False

def producto_entre(rango1init,rango1end, rango2init, rango2end):
    productos = []
    for i in range(rango1init,rango1end):
        for j in range(rango2init,rango2end):
            jejox = i*j
            if nro_palindromo(jejox): productos.append(jejox)
    return productos

print(max(producto_entre(100,999,100,999)))
