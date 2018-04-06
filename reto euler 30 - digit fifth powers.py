# Digit fifth powers
# Problem 30 
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def is_fifth_power(num):
    str_num = str(num)

    lista = []

    for digit in str_num:
        lista.append(int(digit) **5)
    
    return sum(lista) == num

fifth_powers = []

for num in range(1,1000000):
    if is_fifth_power(num): fifth_powers.append(num)

print((fifth_powers))
