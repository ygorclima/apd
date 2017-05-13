from elenco import Elenco

def ShowMenu():
    print ("\n =========== MENU ELENCO ============= ")
    print ("1 - Adicionar ator")
    print ("2 - Buscar atores por filme")
    print ("3 - Buscar elenco")
    print ("4 - Buscar elenco por filme")
    print ("5 - Remover elenco")
    print ("6 - Remover todos atores")
    print ("0 - Voltar")
    opc = input("Digite o NÚMERO da opção: ")

    if (opc == "1"):
        Elenco.AdicionarAtor()
        ShowMenu()
    if (opc == "2"):
        Elenco.BuscarAtoresFilme()
        ShowMenu()
    if (opc =="3"):
        Elenco.BuscarElenco()
        ShowMenu()
    if (opc == "4"):
        Elenco.BuscarElencoFilme()
        ShowMenu()
    if (opc == "5"):
        Elenco.RemoverElenco()
        ShowMenu()
    if (opc == "6"):
        Elenco.RemoverTodosElenco()
    else:    
        ShowMenu()
##    ShowMenu()
##ShowMenu()
