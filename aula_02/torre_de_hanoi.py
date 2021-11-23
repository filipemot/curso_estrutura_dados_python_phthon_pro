contagem_chamadas_recursivas = 0


def _torre_hanoi_recursivo(numero_discos, origem, destino, auxiliar):
    """
    f(n) = 1 + 2 * f(n-1)
    f(n) = 1 + 2 * (1+2* f(n-2)) -> 1 + 2 + 4 * f(n-2)
    f(n) = 1 + 2 + 4 * (1 + 2 * f(n-3)) -> 1 + 2 + 4 + 8 * f(n-3)
    f(n) = 1 + 2 + 4 + ... 2**(n-1)    (I)
    2 * f(n) = 2 + 4 + 8 ... 2 ** n    (II)
    f(n) = 2** n -1                   II - I

    """

    global contagem_chamadas_recursivas
    contagem_chamadas_recursivas = contagem_chamadas_recursivas + 1

    if numero_discos == 1:
        print(f'{origem} -> {destino} : {numero_discos}')
        return

    _torre_hanoi_recursivo(numero_discos - 1, origem, auxiliar, destino)
    print(f'{origem} -> {destino} : {numero_discos}')
    _torre_hanoi_recursivo(numero_discos - 1, auxiliar, destino, origem)


def torre_de_hanoi(numero_discos: int):
    global contagem_chamadas_recursivas
    contagem_chamadas_recursivas = 0
    _torre_hanoi_recursivo(numero_discos, origem='A', destino='C', auxiliar='B')


if __name__ == '__main__':
    for i in range(1, 5):
        print(f'#### Hanoi para {i} discos')
        torre_de_hanoi(i)
        print(f'##### Quantidade de chamadas: {contagem_chamadas_recursivas} chamadas')
