from sala import ControllerSala

def AdicionarSala():
    cod_sala = int(input("Código Sala: "))
    lotacao = input("Lotação: ")
    ControllerSala.AdicionarSala(cod_sala,lotacao)

def StatusOcupada():
    cod_sala = int(input("Código Sala: "))
    ControllerSala.StatusOcupada(cod_sala)

def StatusLivre():
    cod_sala = int(input("Código Sala: "))
    ControllerSala.StatusLivre(cod_sala)

def BuscarSala():
    cod_sala = int(input("Código Sala: "))
    ControllerSala.BuscarSala(cod_sala)

def ListarSalas():
    ControllerSala.ListarSalas()

def RemoverSala():
    cod_sala = int(input("Código Sala: "))
    ControllerSala.RemoverSala(cod_sala)

def RemoverTodasSalas():
    ControllerSala.RemoverTodasSalas()
