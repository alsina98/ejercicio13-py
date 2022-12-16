from functools import reduce

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def imp(x):
    return x % 2

resultado = filter(imp, lista)

lista_imp = list(resultado)

print(lista_imp)

sum = reduce(lambda a, b: a + b, lista_imp)

print(sum)