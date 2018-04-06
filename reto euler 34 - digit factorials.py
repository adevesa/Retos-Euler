# Digit factorials
# Problem 34 
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

def is_factorial_digit(num):
    str_num = str(num)

    lista = [lista_factoriales[int(digit)] for digit in str_num]

    return sum(lista) == num

lista_factoriales = { 
    0:1,
    1:1,
    2:2,
    3:6,
    4:24,
    5:120,
    6:720,
    7:5040,
    8:40320,
    9:362880}

numeros = [x for x in range(3,1000000) if is_factorial_digit(x)]

print(numeros)

print(sum(numeros))