from sessao import Sessao
# from sessao import ControllerSessao
def ShowMenu():
    print ("\n =========== MENU SESSÃO ============= ")
    print ("1 - Criar sessão")
    print ("2 - Recuperar sessão")
    print ("3 - Verificar lotação")
    print ("4 - Listar sessões")
    print ("5 - Remover sessão")
    print ("6 - Remover todos ingressos")
    print ("0 - Voltar")
    opc = input("Digite o NÚMERO da opção: ")
    #ControllerSessao.IniciarSessao()
    if (opc == "1"):
        Sessao.CriarSessao()
        ShowMenu()
    if (opc == "2"):
        Sessao.RecuperarSessao()
        ShowMenu()
    if (opc =="3"):
        Sessao.VerificarLotacao()
        ShowMenu()
    if (opc == "4"):
        Sessao.ListarSessao()
        ShowMenu()
    if (opc == "5"):
        Sessao.RemoverSessao()
        ShowMenu()
    if (opc == "6"):
        Sessao.RemoverTodosSessao()
        ShowMenu()
    if (opc == "0"):
        return (opc)
    else:
        ShowMenu()
