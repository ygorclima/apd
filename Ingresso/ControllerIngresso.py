ingressos = []
#ingressos_meia = []

def IngressoMeia(cod_sessao):
    ing = [cod_sessao, "meia"]
    ingressos.append(ing)
    print (" ===== Ingresso Meia Cadastrado ===== ")
    
def Ingresso(cod_sessao):
    ing = [cod_sessao, "inteiro"]
    ingressos.append(ing)
    print (" ===== Ingresso Cadastrado ====== ")
    
def ListarIngressoVendidos(cod_sessao):
    pass

def ListarIngresso():
    for i in ingressos:
        print ("Ingresso: ",i)
    
def BuscaIngresso(cod_ingresso):
    for i in ingressos:
        if (i[0] == cod_ingresso):
            print (i)
            
    return None

def RemoverIngresso(cod_ingresso):
    for i in ingressos:
        if (i[0] == cod_ingresso):
            ingressos.remove(i)
            print (" ==== Ingresso removido ====")
            return True
    print (" ==== Ingresso não encontrado ===== ")
    return False
            
def RemoverTodosIngresso():
    global ingressos
    ingressos = []
    print (" ====== Ingressos removidos ======= ")
    return ingressos

def IniciarIngresso():
    Ingresso(1)
    Ingresso(2)
