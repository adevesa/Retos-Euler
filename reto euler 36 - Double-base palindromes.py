'''
Double-base palindromes
Problem 36 
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

def es_palindromo(num):
    num_str = str(num) if type(num) == type(1) else num
    reverso = num_str[::-1]

    return num_str == reverso

def to_binary(num):
    return str(bin(num))[2::]

lista = [x for x in range(1,1000001) if es_palindromo(x) and es_palindromo(to_binary(x))]

print(lista)
print(sum(lista))



