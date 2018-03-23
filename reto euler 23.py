'''
Non-abundant sums
Problem 23 
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

import math

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

def is_abundant_number(n):
    return sum(list(divisorGenerator(n))[:-1:]) > n

all_abundant_numbers = [x for x in range(1,28124) if is_abundant_number(x)] 

todos_number = [x for x in range(1,28124)]

def number_mas_cercano(n,lista):
    while True:
        if n in lista: return n
        else: n -= 1

def is_sum_between_two_abundant_number(n):
    n = number_mas_cercano(n,all_abundant_numbers)
    ind = all_abundant_numbers.index(n)

    for x in all_abundant_numbers[ind::]:
        for y in all_abundant_numbers[ind::]:
            if x+y == n : return True
    return False

filtrados = list(filter(is_sum_between_two_abundant_number,todos_number))

print(filtrados)