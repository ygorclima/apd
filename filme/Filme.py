from filme import ControllerFilme

def CadastrarFilme():
    cod_filme = int(input("Código filme: "))
    titulo = input("Título: ")
    duracao = input("Duração: ")
    classificacao = input("Classificação: ")
    diretor = input("Diretor: ")
    distribuidora = input("Distribuidora: ")
    status = input("Status: ")
    genero = input("Gênero: ")
    ControllerFilme.CadastrarFilme(cod_filme,titulo,duracao,classificacao,diretor,distribuidora,status,genero)

def BuscarFilme():
    cod_filme = int(input("Código Filme: "))
    ControllerFilme.BuscarFilme(cod_filme)
    
def ListarFilmes():
    ControllerFilme.ListarFilmes()

def RemoverTodosFilmes():
    ControllerFilme.RemoverTodosFilmes()
