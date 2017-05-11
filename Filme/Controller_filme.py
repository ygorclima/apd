import Filme


def opcao2():
    buscar = str(input("Digite o cod do filme: "))
    volta= Filme.buscar_filme(buscar)
    if volta == None:
        print (" \n \n ========= FILME NAO ENCONTRADO ============")

def opcao1():
    cod_filme=str(input("Digite o codigo: "))
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
