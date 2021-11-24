## Sequencia Mutavel
print("#### Mutavel")
lista = list()

print(id(lista))
print(lista)
lista.append(1)
print(id(lista))
print(lista)

print("\n#### Imutavel")
## Sequencia Imutavel
tupla = (1, 3)
print(id(tupla))
tupla += (2, 4)
print(id(tupla))


print("\n#### String")
a = 'Filipe'
print(id(a))
a= a.replace('i', 'e')
print(id(a))