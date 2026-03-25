# perguntas = [
#         {
#             'Pergunta' : 'Quanto é 2*2',
#             'Opções' : ['1', '2','4','8'],
#             'Resposta' : '4',
#         },
#         {
#             'Pergunta' : 'Quanto é a raiz quadrada de 9',
#             'Opções' : ['2', '3','4,5','6'],
#             'Resposta': '3'
#         },
#         {
#             'Pergunta' : 'Qual a traducao de reliable',
#             'Opções' : ['Confiante', 'Confiavel','Reliquia','Obrigado'],
#             'Resposta' : 'Confiavel'
#         },
# ]

# print(f"Pergunta: {perguntas[0]['Pergunta']}?")
# print()
# print("Opções:")
# for i, opcao in enumerate(perguntas[0]['Opções']):
#     print(f"{i}) {opcao}")
# indice_1 = input("Escolha uma opção: ")

# acertos = 0
# total_questoes=0

# if indice_1 == "2":
#     acertos +=1
#     total_questoes+=1
#     print("Você acertou")
# else:
#     print ("Voce errou")
#     total_questoes+=1

# print (f"Pergunta: {perguntas[1]['Pergunta']}?")
# print()
# print("Opções:")
# for i, opcao in enumerate(perguntas[1]['Opções']):
#     print(f"{i}) {opcao}")
# indice_2 = input("Escolha uma opção: ")

# if indice_2 == "1":
#     acertos+=1
#     total_questoes+=1
#     print("Voce acertou!")
# else:
#     print("Voce errou!")
#     total_questoes+=1

# print(f"Pergunta: {perguntas[2]['Pergunta']}?")
# print()
# print(f"Opções:")
# for i, opcao in enumerate(perguntas[2]['Opções']):
#     print(f"{i}) {opcao}")
# indice_3 = input("Escolha uma opção: ")

# if indice_3 == "0":
#     acertos += 1
#     total_questoes+=1
#     print("Voce acertou")
# else:
#     print("Voce errou!")
#     total_questoes+=1

# print(f"Voce acertou {acertos} de {total_questoes} perguntas")




perguntas = [
    {
        'Pergunta': 'Quanto é 2*2',
        'Opções': ['1', '2', '4', '8'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é a raiz quadrada de 9',
        'Opções': ['2', '3', '4,5', '6'],
        'Resposta': '3'
    },
    {
        'Pergunta': 'Qual a traducao de reliable',
        'Opções': ['Confiante', 'Confiavel', 'Reliquia', 'Obrigado'],
        'Resposta': 'Confiavel'
    },
]

acertos = 0
total_questoes = 0

for pergunta in perguntas:
    print(f"Pergunta: {pergunta['Pergunta']}?")
    print()
    print("Opções:")
    for i, opcao in enumerate(pergunta['Opções']):
        print(f"{i}) {opcao}")

    escolha = input("Escolha uma opção: ")

    if pergunta['Opções'][int(escolha)] == pergunta['Resposta']:
        print("Voce acertou")
        acertos+=1
    else:
        print("Você errou! ❌")

    total_questoes += 1
    print()

print(f"Você acertou {acertos} de {total_questoes} perguntas")




