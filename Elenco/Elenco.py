from elenco import ControllerElenco
from ator import ControllerAtor
##from filme import ControllerFilme

def AdicionarAtor():
    cod_elenco = int(input("Código: "))
    cod_ator = int(input("Código Ator: "))
    r = ControllerAtor.BuscarAtor(cod_ator)
    if (r == None):
        print ("Ator não existe")
        return (r)   
    cod_filme = int(input("Código Filme: "))

    r = ControllerFilme.BuscarFilme(cod_filme)
    if (r == None):
        print ("Filme não existe")
        return (r)
    
    tipo = input("Tipo: ")
    
    ControllerElenco.AdicionarAtor(cod_elenco,cod_ator,cod_filme,tipo)

def BuscarAtoresFilme():
    cod_elenco = int(input("Código Elenco: "))
    ControllerElenco.BuscarAtoresFilme(cod_elenco)

def BuscarElenco():
    cod_elenco = int(input("Código Elenco: "))
    ControllerElenco.BuscarElenco(cod_elenco)

def BuscarElencoFilme():
    cod_filme = int(input("Código Filme: "))
    ControllerElenco.BuscarElencoFilme(cod_filme)

def RemoverElenco():
    cod_elenco = int(input("Código Elenco: "))
    ControllerElenco.RemoverElenco(cod_elenco)

def RemoverTodosElenco():
    ControllerElenco.RemoverTodosElenco()
