from collections import Counter
from itertools import cycle
from time import perf_counter_ns

lista_numeros = list(range(10))
print(id(lista_numeros))
print(id(lista_numeros[0]))
print(id(lista_numeros[1]))
print(id(lista_numeros[2]))

id_inicial = id(lista_numeros)
print(f'###{id_inicial}')
counter = Counter()
maior_delta = 0

for i in cycle([11,12]):
    id_final = id(lista_numeros)
    inicio = perf_counter_ns()
    lista_numeros.append(i)
    delta = perf_counter_ns() - inicio
    counter[delta//200] += 1
    print(counter)


