sala = []

def AdicionarSala(cod_sala,lotacao):
    aux = [cod_sala,lotacao]
    sala.append(aux)
    print (" === Sala adicionada === ")
    
def StatusOcupada(cod_sala):
    for s in sala:
        if (s[0] == cod_sala):
            s[1] = "Ocupada"
        return s
    return None
def StatusLivre(cod_sala):
    for s in sala:
        if (s[0] == cod_sala):
            s[1] = "Ocupada"
        return s
    return None

def BuscarSala(cod_sala):
    for s in sala:
        if (s[0] == cod_sala):
            print (s)
            return s
    return None

def ListarSala():
    global sala
    print (sala)
    return sala

def RemoverSala(cod_sala):
    for s in sala:
        if (s[0] == cod_sala):
            sala.remove(s)
            print (" ==== Sala removida === ")
            return True
    return False
def RemoverTodasSalas():
    global sala
    sala = []
    return sala

def IniciarSala():
    AdicionarSala(1,"livre")
    AdicionarSala(2,"ocupada")
