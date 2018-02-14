a = []

indice = 1

def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return (fibonacci(n-1)+fibonacci(n-2))

while(n <= 4000000):
    indice = indice + 1
    n = fibonacci(indice)

print(indice)


print(fibonacci(5))
