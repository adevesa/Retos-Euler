'''
Names scores
Problem 22 
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''
import re
from string import ascii_lowercase,ascii_uppercase

arch = open("PATHHHHHHHHHHHHHHHHHHHHHH","r")
string = arch.read()
string = re.sub('"','',string)
string = string.split(',')
string = sorted(string)

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

num = 0
lim = len(string)
while(num != lim):
    string[num] = string_to_num(string[num])
    string[num] *= num + 1
    num += 1

print(sum(string))
