def potencia_interativa(base: int, expoente: int):
    resultado = 1
    for _ in range(expoente):
        resultado *= base
    return resultado


def _potencia_interativa_resursiva(base, expoente, resultado=1):
    if expoente == 0:
        return resultado

    return _potencia_interativa_resursiva(base, expoente - 1, resultado * base)


def potencia_interativa_resursiva(base: int, expoente: int):
    """
    O(n) para tempo de execução
    f(n) = 4 + f(n-1)
    f(n) = 4 + 4 + f(n-2)
    f(n) = 4 + 4 + 4 + f(n-3)
    f(n) = 4 * n

    O(n) para tempo de execução
    O(n) para memória


    :param base:
    :param expoente:
    :return:
    """

    return _potencia_interativa_resursiva(base, expoente - 1, base)


def _potencia_recursiva_logaritmica(base: int, expoente: int, resultado=1):
    """
    base ** expoente =  se expoente é par: base ** (2 * n), onde n é expoente //2
                        Simplificando (base ** 2) ** n

                        Caso contrário expoente = 2 * n + 1 base ** (2 * n + 1)
                        base ** (2*n +1) -> base * (base ** (2*n)) = base * [(base * base) ** n]

    O(log n) para tempo de execução

    :param base:
    :param expoente:
    :return:
    """
    if expoente == 0:
        return resultado

    if expoente % 2 == 0:
        return _potencia_recursiva_logaritmica(base * base, expoente // 2, resultado)
    else:
        resultado *= base
        return _potencia_recursiva_logaritmica(base, expoente - 1, resultado)


def potencia_recursiva_logaritmica(base: int, expoente: int):
    return _potencia_recursiva_logaritmica(base, expoente)


if __name__ == '__main__':
    print(potencia_interativa(2, 10))
    print(potencia_interativa_resursiva(2, 10))
    print(potencia_recursiva_logaritmica(2, 5))
