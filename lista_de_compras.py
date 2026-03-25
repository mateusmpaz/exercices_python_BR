import os

lista_compras = []
while True:
    escolha = input("Selecione uma opção\n[I]nserir [a]pagar [l]istar [s]air: ")
    escolha = escolha.lower()
    indice_lista = len(lista_compras)


    if escolha == "i" or escolha == "inserir":
        os.system("cls")
        novo_valor = input("Valor:")
        lista_compras.append(novo_valor)
        

    elif escolha == "l" or escolha == "listar":
        os.system("cls")

        if len(lista_compras) == 0:
            print("Nada à mostrar")
             
        for indice, item in enumerate(lista_compras):
            print(indice, item)


    elif escolha == "a" or escolha == "apagar":
        os.system("cls")
        try:
            indice = int(input("Qual indice deseja apagar: "))
            if indice < len(lista_compras) and indice >= 0:
                lista_compras.pop(indice)
                print("INDICE APAGADO COM SUCESSO")
            else:
                print("Voce excedeu o numero maximo da lista!")
                
        except ValueError:
            print("Digite apenas numeros!")
            
        

    elif escolha == "s" or escolha == "sair":
        os.system("cls")
        print ("VOCE DEDICIU SAIR DO PROGRAMA")
        break



    else:
        print("Essa opção nao é valida")