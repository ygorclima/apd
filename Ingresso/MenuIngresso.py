from ingresso import Ingresso
#from ingresso import ControllerIngresso
def ShowMenu():
    print ("\n =========== MENU INGRESSO ============= ")
    print ("1 - Venda Ingresso Meia")
    print ("2 - Venda Ingresso Inteira")
    print ("3 - Listar ingresso inteiro")
    print ("4 - Listar ingresso")
    print ("5 - Buscar ingresso")
    print ("6 - Remover ingresso")
    print ("7 - Remover Todos Ingresso")
    print ("0 - Voltar")
    opc = input("Digite o NÚMERO da opção: ")
    #ControllerIngresso.IniciarIngresso()
    if (opc == "1"):
        Ingresso.IngressoMeia()
        ShowMenu()
    if (opc == "2"):
        Ingresso.Ingresso()
        ShowMenu()
    if (opc == "3"):
        Ingresso.ListarIngressoVendidos()
        ShowMenu()
    if (opc == "4"):
        Ingresso.ListarIngresso()
        ShowMenu()
    if (opc == "5"):
        Ingresso.BuscaIngresso()
        ShowMenu()
    if (opc == "6"):
        Ingresso.RemoverIngresso()
        ShowMenu()
    if (opc == "7"):
        Ingresso.RemoverTodosIngresso()
    if (opc == "0"):
        return (opc)
    else:
        ShowMenu()
    
