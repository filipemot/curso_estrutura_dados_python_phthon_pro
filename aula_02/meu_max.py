from math import inf
from time import time


def meu_max(interavel):
    numero_max = -inf

    for numero in interavel:
        if numero > numero_max:
            numero_max = numero
    return numero_max

if __name__ == '__main__':
    print(meu_max([1]))

    print('Estudo Experimental sobre o tempo de execução da função max')

    inicio = 1_000_000
    for n in range(0, inicio * 20 + 1, inicio):
        inicio_execucao = time()
        meu_max(range(n))
        fim_execucao = time()
        tempo_execucao_segundos = fim_execucao - inicio_execucao
        print('*' * int(tempo_execucao_segundos * 10), n)



