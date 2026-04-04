# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.

def zipper():
    resultado = []
    for i in range(len(lista_menor)):
        resultado.append((lista_menor[i], lista_maior[i]))
    return resultado



lista_city = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_state = ['BA', 'SP', 'MG', 'RJ']


if len(lista_city)  < len(lista_state):
    lista_menor = lista_city
    lista_maior = lista_state
else:
    lista_menor = lista_state
    lista_maior = lista_city

print(zipper())


def zipper():
    resultado = []

    for cidade, estado in zip(lista_city,lista_state):
        resultado.append((cidade, estado))
    return resultado




lista_city = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_state = ['BA', 'SP', 'MG', 'RJ']

print(zipper())

def zipper(l1, l2):

    intervalo_maximo = min(len(l1),len(l2))

    return [
        (l1[i],l2[i]) for i in range(intervalo_maximo) 


    ]

lista_city = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_state = ['BA', 'SP', 'MG', 'RJ']

print(zipper(lista_city, lista_state))

l1 =    ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 =    ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l1,l2)))