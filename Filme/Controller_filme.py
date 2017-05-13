import Filme

# Função que busca o filme pelo código
def BuscarFilme(cod_filme):
    for f in Filme:
        if (f[0] == cod_filme):
            return (f)
    return None

def opcao2():
    buscar = str(input("Digite o cod do filme: "))
    volta= Filme.buscar_filme(buscar)
    if volta == None:
        print (" \n \n ========= FILME NAO ENCONTRADO ============")
    else:
        print (volta)

def opcao1():
    cod_filme=str(input("Digite o codigo: "))#testando
    consulta=Filme.buscar_filme(cod_filme)
    while consulta != None:
        cod_filme=str(input("Digite o codigo valido: "))
        consulta=Filme.buscar_filme(cod_filme)
    titulo=str(input("Digite a Titulo: "))
    duracao=str(input("Digite a Duracao: "))
    classificacao=str(input("Digite a classificacao: "))
    diretor=str(input("Digite o Diretor: "))
    distribuidora=str(input("Digite a Distribuidora: "))
    status=str(input("Digite o Status: "))
    genero=str(input("Digite o Genero: "))
    Filme.cadastrar_filme(cod_filme,titulo,duracao,classificacao,diretor,distribuidora,status,genero)

def opcao3():
    Filme.listar_filmes()

def opcao4 ():
    print (" \n \n ========= DESEJA EXCLUIR TODAS OS FILMES ?? ============\n")
    excluir_t=str(input("S ou N: "))
    if excluir_t == 'S' or excluir_t == 's':
        Filme.remover_todos_filmes()
    else:
        return None
