from math import inf
from time import time


def meu_max(interavel):
    """
    Análise de algoritmo
    Tempo de execução, algoritmo 0(n)
    Em memória 0(1)
    :param interavel:
    :return:

    f(n) = 2 + 4*n  ---> 0(n)
    """
    numero_max = -inf  # 1

    for numero in interavel:  # 1
        if numero > numero_max:  # 1
            numero_max = numero  # 1
    return numero_max  # 1


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
