##from Sala import menu_sala
##from Filme import menu_filme
from Elenco import *
import Ator

def ShowMenu():
    print ("\n =========== MENU PRINCIPAL ============= ")
    print ("1 - Acessar Menu Ator")
    print ("2 - Acessar Menu Elenco")
    print ("3 - Acessar Menu Sala")
    print ("4 - Acessar Menu Filme")
    print ("0 - Finalizar programa")
    opc = input("Digite o NÚMERO da opção: ")

    if (opc == "1"):MenuAtor.ShowMenu()
    if (opc == "2"):MenuElenco.ShowMenu()
##    if (opc == "3"):menu_sala()
##    if (opc == "4"):menu_filme()
    if (opc == "0"):return
    
ShowMenu()
