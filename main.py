import sys
from ator import MenuAtor
from elenco import MenuElenco
##from sala import menu_sala
##from filme import menu_filme

def ShowMenus():
    print ("\n =========== MENU PRINCIPAL ============= ")
    print ("1 - Acessar Menu Ator")
    print ("2 - Acessar Menu Elenco")
    print ("3 - Acessar Menu Sala")
    print ("4 - Acessar Menu Filme")
    print ("0 - Finalizar programa")
    opc = input("Digite o NÚMERO da opção: ")

    if (opc == "1"):
        MenuAtor.ShowMenu()
        ShowMenus()
    if (opc == "2"):
        MenuElenco.ShowMenu()
        ShowMenus()
    if (opc == "3"):
        menu_sala()
        ShowMenus()
    if (opc == "4"):
        menu_filme()
        ShowMenus()
    
ShowMenus()
