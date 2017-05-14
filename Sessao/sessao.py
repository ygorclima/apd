from sessao import ControllerSessao
from filme import Controller_filme
from sala import Sala

def CriarSessao():
    cod_sessao = int(input("Código Sessão: "))
    cod_filme = int(input("Código Filme: "))
    r = Controller_filme.BuscarFilme(cod_filme)
    if (r == None):
       print ("Filme não existe")
       return (r)
    cod_sala = int(input("Código Sala: "))
    r = Sala.buscar_sala(cod_sala)
    if (r == None):
        print ("Sala não existe")
        return (r)
    horario = input("Horário: ")
    ControllerSessao.CriarSessao(cod_sessao,cod_filme,cod_sala,horario)
def RecuperarSessao():
    cod_sessao = int(input("Código Sessão: "))
    ControllerSessao.RecuperarSessao(cod_sessao)
    
def VerificarLotacao():
    cod_sessao = int(input("Código Sessão: "))
    ControllerSessao.VerificarLotacao(cod_sessao)
    
def ListarSessao():
    ControllerSessao.ListarSessao()
    
def RemoverSessao():
    cod_sessao = int(input("Código Sessão: "))
    ControllerSessao.RemoverSessao(cod_sessao)
    
def RemoverTodosSessao():
    ControllerSessao.RemoverTodosSessao()
