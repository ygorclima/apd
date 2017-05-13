from ator import Ator
from ator import ControllerAtor

def ShowMenu():
    print ("\n =========== MENU ator ============= ")
    print ("1 - Cadastrar ator")
    print ("2 - Buscar ator")
    print ("3 - Buscar todos atores")
    print ("4 - Remover ator")
    print ("5 - Remover todos atores")
    print ("0 - Voltar")
    opc = input("Digite o NÚMERO da opção: ")

    if (opc == "1"):
        Ator.CadastrarAtor()
        ShowMenu()
    elif (opc == "2"):
        Ator.BuscarAtor()
        ShowMenu()
    elif (opc == "3"):
        Ator.BuscarAtores()
        ShowMenu()
    elif (opc == "4"):
        Ator.RemoverAtor()
        ShowMenu()
    elif (opc == "5"):
        Ator.RemoverTodosAtores()
        ShowMenu()
    elif (opc == "0"):
        return (opc)
##    ShowMenu()
#Controllerator.IniciarAtores()
##ShowMenu()
