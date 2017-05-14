sessao = []

def CriarSessao(cod_sessao,cod_filme,cod_sala,horario):
    aux = [cod_sessao,cod_filme,cod_sala,horario]
    sessao.append(aux)
    print (" ===== Sessão Adicionada ====== ")
    
def RecuperarSessao(cod_sessao):
    for s in sessao:
        if (s[0] == cod_sessao):
            print (s)
            return s
    return None

def VerificarLotacao(cod_sessao):
    pass

def ListarSessao():
    global sessao
    print (sessao)
    return sessao

def RemoverSessao(cod_sessao):
    for s in sessao:
        if (s[0] == cod_sessao):
            sessao.remove(s)
            print (" ==== Sessão Removida ==== ")
            return True
    print (" === Sessão não encontrada ==== ")
    return False

def RemoverTodosSessao():
    global sessao
    sessao = []
    print (" ==== Todas as sessões removidas ==== ")
    return sessao

def IniciarSessao():
    CriarSessao(1,1,1,"8:30")
    CriarSessao(2,1,1,"9:00")
    
    
