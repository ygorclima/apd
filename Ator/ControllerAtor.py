atores = []

##codigo_geral = 0
##
##def _gerar_codigo():
##    global codigo_geral
##    codigo_geral += 1
##    return codigo_geral

def CadastrarAtor(cod_ator,nome,nacionalidade,idade):
    #cod_ator = _gerar_codigo()
    
    ator = [cod_ator,nome,nacionalidade,idade]
    atores.append(ator)
    print (" \n \n ========= Ator cadastrado ============")
    
def BuscarAtor(cod_ator):
    for a in atores:
        if (a[0] == cod_ator):
            print (a)
            return a
    return None

def BuscarAtores():
    global atores
    print(atores)
    return atores
        
def RemoverAtor(cod_ator):
    for a in atores:
        if (a[0] == cod_ator):
            atores.remove(a)
            print("\n \n ========== Ator removido ==========")
            return True
    print ("\n \n ========= Ator não encontrado ===========")
    return False

def RemoverTodosAtores():
    global atores
    atores = []
    print ('\n \n  ========== Atores removidos =========== ')
    return atores

def IniciarAtores():
    CadastrarAtor(1,"Messias","Brasileiro",21)
    CadastrarAtor(2,"Ygor","Brasileiro",20)
    CadastrarAtor(3,"Guilherme","Brasileiro",18)

