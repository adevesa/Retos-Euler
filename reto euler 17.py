##Number letter counts
##Problem 17 
##If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
##
##If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
##
##
##NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

def traductor(n):
    if n == 1 : return "one"
    if n == 2 : return "two"
    if n == 3 : return "three"
    if n == 4 : return "four"
    if n == 5 : return "five"
    if n == 6 : return "six"
    if n == 7 : return "seven"
    if n == 8 : return "eight"
    if n == 9 : return "nine"
    if n == 10: return "ten"
    if n == 11: return "eleven"
    if n == 12: return "twelve"
    if n == 13: return "thirteen"
    if n == 14: return "fourteen"
    if n == 15: return "fifteen"
    if n == 16: return "sixteen"
    if n == 17: return "seventeen"
    if n == 18: return "eighteen"
    if n == 19: return "nineteen"
    if n == 20: return "twenty"
    if n == 30: return "thirty"
    if n == 40: return "forty"
    if n == 50: return "fifty"
    if n == 60: return "sixty"
    if n == 70: return "seventy"
    if n == 80: return "eighty"
    if n == 90: return "ninety"
    if n == 100: return "a hundred"
    if n == 1000: return "thousand"

def separar_numeros(n):
    if n == 1000: return "thousand"
    cuantos_cientos = int(n/100)
    cuantas_decenas = int(n%100 / 10)
    cuantas_unidades = (n%100 % 10)

    return cuantos_cientos, cuantas_decenas, cuantas_unidades

def armar_frase(n):
    frase = ""
    if n == 1000: return "onethousand"
    c,d,u = separar_numeros(n)
    if c != 0 and (d != 0 or u !=0): frase = frase + traductor(c) + "hundred" + "and" 
    if c != 0 and d == 0 and u == 0: frase = frase + traductor(c) + "hundred"
    if d != 0 and u==0: frase = frase + traductor(d*10)
    if d == 1 and u !=0: frase = frase + traductor(d*10+u)
    if d != 0 and d != 1 and u !=0: frase = frase + traductor(d*10) + traductor(u)
    if d == 0 and u !=0: frase = frase + traductor(u)

    return frase

def problema():
    contador = 0
    for i in range(1,1001):
       ##print(str(i) + "-" + armar_frase(i))
       contador = contador + len(armar_frase(i))
    return contador
print(problema())
        
    
