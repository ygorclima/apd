#import ControllerAtor
import Ator

def ShowMenu():
    print ("\n =========== MENU ATOR ============= ")
    print ("1 - Cadastrar Ator")
    print ("2 - Buscar ator")
    print ("3 - Buscar todos atores")
    print ("4 - Remover ator")
    print ("5 - Remover todos atores")
    print ("0 - Voltar")
    opc = input("Digite o NÚMERO da opção: ")

    if (opc == "1"):Ator.CadastrarAtor()
    elif (opc == "2"):Ator.BuscarAtor()
    elif (opc == "3"):Ator.BuscarAtores()
    elif (opc == "4"):Ator.RemoverAtor()
    elif (opc == "5"):Ator.RemoverTodosAtores()
    elif (opc == "0"):MenuPrincipal()
    ShowMenu()
#ControllerAtor.IniciarAtores()
ShowMenu()
