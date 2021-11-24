def gerar_ponto():
    return 1, 2


primeiro, segundo = gerar_ponto()

print(primeiro, segundo)


def argumentos_variaveis(*args):
    print(args)
    print(type(args))


argumentos_variaveis(1, 2)
argumentos_variaveis(*'ab') ##Desempacotamento

for chave, valor in {'pt': 'Portugues', 'en': 'Ingles'}.items():
    print(chave, valor)
