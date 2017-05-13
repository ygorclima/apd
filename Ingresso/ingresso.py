from ingresso import ControllerIngresso

def IngressoMeia():
    cod_sessao = int(input("Código Sessão: "))
    ControllerIngresso.IngressoMeia(cod_sessao)
    
def Ingresso():
    cod_sessao = int(input("Código Sessão: "))
    ControllerIngresso.Ingresso(cod_sessao)
    
def ListarIngressoVendidos():
    cod_sessao = int(input("Código Sessão: "))
    ControllerIngresso.ListarIngressoVendidos(cod_sessao)
def ListarIngresso():
    ControllerIngresso.ListarIngresso()
    
def BuscaIngresso():
    cod_ingresso = int(input("Código Ingresso: "))
    ControllerIngresso.BuscaIngresso(cod_ingresso)
    
def RemoverIngresso():
    cod_ingresso = int(input("Código Ingresso: "))
    ControllerIngresso.RemoverIngresso(cod_ingresso)
    
def RemoverTodosIngresso():
    ControllerIngresso.RemoverTodosIngresso()
