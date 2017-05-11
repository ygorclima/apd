elencos = []

def AdicionarAtor(cod_elenco,cod_ator,cod_filme,tipo):
    elenco = [cod_elenco,cod_ator,cod_filme,tipo]
    elencos.append(elenco)
    print ("\n \n ======== Ator adicionado ======= ")
    
def BuscarTodosElenco():
    global elencos
    print(elencos)
    return elencos

def BuscarAtoresFilme(cod_elenco):
    for e in elencos:
        if (e[0] == cod_elenco):
            print (e)
            return e
    return None

def BuscarElenco(cod_elenco):
    for e in elencos:
        if (e[1] == cod_elenco):
            print (e)
            return e
    return None

def BuscarElencoFilme(cod_filme):
    for e in elencos:
        if(e[2]==cod_filme):
            print (e)
            return e
    return None

def RemoverElenco(cod_elenco):
    for e in elencos:
        if(e[0]== cod_elenco):
            elencos.remove(e)
            print (" \n \n ======= Elenco removido ====== ")
            return True
    print ("\n \n ========== Ator não encontrado ========= ")
    return False

def RemoverTodosElenco():
    global elencos
    elencos = []
    print ("\n \n ======= Todos os elencos removidos ======== ")
    return elencos

def IniciarElenco():
    AdicionarAtor(1,1,1,"principal")
    AdicionarAtor(2,2,2,"principal")
