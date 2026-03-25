import re
import sys

while True:

    cpf_da_pessoa = re.sub(r"\D", "" , input("Digite seu CPF: "))

    if not cpf_da_pessoa.isdigit():
        print("Parece que voce nao digitou apenas numeros!")
        continue 

    if len(cpf_da_pessoa) != 11:
        print("Voce nao digitou o numero correto")
        continue

    sequencia_de_numeros = cpf_da_pessoa == cpf_da_pessoa[0] * len(cpf_da_pessoa)

    if sequencia_de_numeros:
        print("Voce enviou dados sequencias")
        sys.exit()


    nove_digitos = cpf_da_pessoa[:9]
    soma_dos_9_numeros = 0
    contador_regressivo = 10

    for numero in nove_digitos:
        soma_dos_9_numeros += int(numero) * contador_regressivo
        contador_regressivo -= 1 
    
    soma_vezes_10 = soma_dos_9_numeros * 10
    resto_divisao = soma_vezes_10 % 11

    if resto_divisao > 9:
        primeiro_digito = 0
    else:
        primeiro_digito = resto_divisao

    if primeiro_digito == int(cpf_da_pessoa[9]):
        print("Primeiro digito valido!")
    else:
        print("Primeiro digito invalido!")
        print(f"O primeiro digito deveria ser {primeiro_digito}")
        continue
    
    #PARTE 2 

    dez_digitos = cpf_da_pessoa[:10]
    soma_dos_10_numeros = 0
    contador_regressivo_2 = 11

    for digito in dez_digitos:
        soma_dos_10_numeros += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1 

    resto_parte2 = ((soma_dos_10_numeros * 10) % 11)

    segundo_digito = resto_parte2 if resto_parte2 <=9 else 0

    if segundo_digito == int(cpf_da_pessoa[10]):
        print("Segundo digito correto")
    else:
        print(f"O segundo digito deveria ser {segundo_digito}")
        continue
    
    print("Parabens, seu CPF foi validado!")

    break
