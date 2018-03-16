'''Counting Sundays
Problem 19 
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?'''

year = 1900
september = april = june = november = range(1,31)
january = march = may = july = august = october = december = range(1,32)
days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
## months = [january,febrero(),march,april,may,june,july,august,september,october,november,december]

def armar_calendario(anio):
    year = anio

    february = range(1,30) if (year % 4 == 0 and (year % 100 != 0 or year %400 == 0)) else range(1,29)

    months = [january,february,march,april,may,june,july,august,september,october,november,december]

    dias = []

    for month in months:
        dias += month

    return dias

def armar_calendario_desde(anioInicio,anioFin):
    dias = []
    for anio in range(anioInicio,anioFin+1):
        dias += armar_calendario(anio)
    retornar = range(1,len(dias)+1)
    return retornar

def armar_n_calendario_desde(anioInicio,anioFin):
    dias = []
    for anio in range(anioInicio,anioFin+1):
        dias += armar_calendario(anio)
    return dias

def map_dias(dias):
    dias_map = []
    for dia in dias:
        dias_map.append(days[(dia -1)%7])

    return dias_map

def cant_domingos(lista):
    cont = 0
    for dia in lista:
        if dia == (1,"sunday"): cont += 1
    return cont

def cuantos_dias_tiene(anio):
    year = anio

    february = range(1,30) if (year % 4 == 0 and (year % 100 != 0 or year %400 == 0)) else range(1,29)

    months = [january,february,march,april,may,june,july,august,september,october,november,december]

    dias = 0
    for month in months:
        dias += len(month)
    return dias

def cuantos_dias_desde_hasta(inicio,fin):
    dias = 0
    for anio in range(inicio,fin+1):
        dias += cuantos_dias_tiene(anio)
    return dias

def cuantos_domingos_hubo(dias):
    return dias / 7


# domingos_de_1900 = cuantos_domingos_hubo(cuantos_dias_tiene(1900))
# domingos_de_1900_2000 = cuantos_domingos_hubo(cuantos_dias_desde_hasta(1900,2000))

# print(domingos_de_1900_2000 - domingos_de_1900)

calendario_n_dias = armar_n_calendario_desde(1900,2000)
print(calendario_n_dias)
calendario_numeros = armar_calendario_desde(1900,2000)
calendario_nombres = map_dias(calendario_numeros)
print(calendario_nombres)

zipeado = zip(calendario_n_dias,calendario_nombres)

domingos_desde_1901 = cant_domingos(list(zipeado)[365::])
print(domingos_desde_1901)







