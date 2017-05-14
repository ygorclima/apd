import sys
from ator import MenuAtor
from elenco import MenuElenco
from sala import MenuSala
from filme import MenuFilme
from ingresso import MenuIngresso
from sessao import MenuSessao
def ShowMenus():
    print ("\n =========== MENU PRINCIPAL ============= ")
    print ("1 - Acessar Menu Ator")
    print ("2 - Acessar Menu Elenco")
    print ("3 - Acessar Menu Sala")
    print ("4 - Acessar Menu Filme")
    print ("5 - Acessar Menu Ingresso")
    print ("6 - Acessar Menu Sessao")
    print ("0 - Finalizar programa")
    opc = input("Digite o NÚMERO da opção: ")

    if (opc == "1"):
        MenuAtor.ShowMenu()
        ShowMenus()
    if (opc == "2"):
        MenuElenco.ShowMenu()
        ShowMenus()
    if (opc == "3"):
        MenuSala.ShowMenu()
        ShowMenus()
    if (opc == "4"):
        MenuFilme.ShowMenu()
        ShowMenus()
    if (opc == "5"):
        MenuIngresso.ShowMenu()
        ShowMenus()
    if (opc == "6"):
        MenuSessao.ShowMenu()
        ShowMenus()
    
ShowMenus()
