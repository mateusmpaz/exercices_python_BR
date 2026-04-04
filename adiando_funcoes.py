# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def criar_funcao(funcao, *args):
    def interna(y):
        return funcao(args[0], y)
    return interna

soma_com_cinco = criar_funcao(soma, 5)
print(soma_com_cinco(3))

multiplica_por_dez = criar_funcao(multiplica, 10)
print(multiplica_por_dez(2))