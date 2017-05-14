from sala import Sala
# from sala import ControllerSala

def ShowMenu():
    print ("\n =========== MENU SALA ============= ")
    print ("1 - Adicionar sala")
    print ("2 - Definir status Ocupada")
    print ("3 - Definir status Livre")
    print ("4 - Buscar sala")
    print ("5 - Listar salas")
    print ("6 - Remover sala")
    print ("7 - Remover todas salas")
    print ("0 - Voltar")
    opc = input("Digite o NÚMERO da opção: ")
    #ControllerSala.IniciarSala()
    if (opc == "1"):
        Sala.AdicionarSala()
        ShowMenu()
    if (opc == "2"):
        Sala.StatusOcupada()
        ShowMenu()
    if (opc =="3"):
        Sala.StatusLivre()
        ShowMenu()
    if (opc == "4"):
        Sala.BuscarSala()
        ShowMenu()
    if (opc == "5"):
        Sala.ListarSalas()
        ShowMenu()
    if (opc == "6"):
        Sala.RemoverSala()
        ShowMenu()
    if (opc == "7"):
        Sala.RemoverTodasSalas()
        ShowMenu()
    if (opc == "0"):
        return (opc)
    else:
        ShowMenu()
