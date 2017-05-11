import ControllerAtor

def CadastrarAtor():
    cod_ator = int(input("Código: "))
    nome = input("Nome: ")
    nacionalidade = input("Nacionalidade: ")
    idade = int(input("Idade: "))

    ControllerAtor.CadastrarAtor(cod_ator,nome,nacionalidade,idade)
    
def BuscarAtor():
    cod_ator = int(input("Código: "))
    ControllerAtor.BuscarAtor(cod_ator)

def BuscarAtores():
    ControllerAtor.BuscarAtores()
        
def RemoverAtor():
    cod_ator = int(input("Código: "))
    ControllerAtor.RemoverAtor(cod_ator)
    
def RemoverTodosAtores():
    ControllerAtor.RemoverTodosAtores()
    
