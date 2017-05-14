from filme import Filme
#from filme import ControllerFilme

def ShowMenu():
    print ("\n =========== MENU FILME ============= ")
    print ("1 - Cadastrar filme")
    print ("2 - Buscar filme")
    print ("3 - Listar filme")
    print ("4 - Remover todos filmes")
    print ("0 - Voltar")
    opc = input("Digite o NÚMERO da opção: ")
    #ControllerFilme.IniciarFilme()
    if (opc == "1"):
        Filme.CadastrarFilme()
        ShowMenu()
    if (opc == "2"):
        Filme.BuscarFilme()
        ShowMenu()
    if (opc == "3"):
        Filme.ListarFilmes()
        ShowMenu()
    if (opc == "4"):
        Filme.RemoverTodosFilmes()
        ShowMenu()
    if (opc == "0"):
        return (opc)
    else:
        ShowMenu()
