'''
Permuted multiples
Problem 52 
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

import re

def pop_char(char, string):
    jejox = re.sub(char,"",string,1)
    return jejox


def son_permutados(num1,num2):
    snum1 = str(num1)
    snum2 = str(num2)

    if len(snum1) != len(snum2): return False
    
    for digit in snum1:
        if digit in snum2: 
            snum2 = pop_char(digit,snum2)
        else: return False
    
    return True

def multiplos_permutados(num):
    for multiplicador in range(2,6+1):
        multiplicado = num * multiplicador
        if not son_permutados(num,multiplicado): return False
    
    return True

n = 2
while not multiplos_permutados(n):
    n += 1

print(n)



