'''
Coded triangle numbers
Problem 42 
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''
import re
from string import ascii_lowercase,ascii_uppercase

direccion = "PATHHHHHHH"

arch = open(direccion,"r")
words = arch.read()
words = re.sub('"','',words)
words = words.split(',')

triangle_numbers = {

}

def is_triangle_number(number):
    return triangle_numbers[number]

def triangle_number(n):
    return 0.5*n*(n+1)

duplas = []
y = 1
for x in ascii_lowercase:
    duplas.append((x,y))
    y +=1
y = 1
for x in ascii_uppercase:
    duplas.append((x,y))
    y+=1
duplas = dict(duplas)

def string_to_num(palabra):
    suma = 0
    for letra in palabra:
        suma += duplas[letra]
    return suma


for i in range(1,1000):
    triangle_numbers.update({triangle_number(i):True})

contador = 0
for word in words:
    try:
         if triangle_numbers[string_to_num(word)]: contador += 1
    except KeyError as e:
        pass


print(contador)




