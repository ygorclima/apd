import Sala

def opcao4():
    buscar = str(input("Digite o cod da sala: "))
    volta= Sala.buscar_sala(buscar)
    if volta == None:
        print (" \n \n ========= SALA NAO ENCONTRADA ============")

        
def opcao1():
    codigo=str(input("Digite o codigo: "))
    consulta=Sala.buscar_sala(codigo)
    while consulta != None:
        codigo=str(input("Digite um codigo Valido: "))
        consulta=Sala.buscar_sala(codigo)
    cap=int(input("Digite a capacidade: "))
    op_status=int(input("\n 1- Ocupado.\n 2- Disponivel \n Digite: "))
    while op_status != 1 and op_status != 2:
        op_status=int(input("DIGITE UMA OPCAO VALIDA: \n 1- Ocupado. \n 2- Disponivel \n"))
    if op_status == 1:
        status= 'Ocupado'
    else:
        status= 'Disponivel'
    Sala.adicionar_sala(codigo,cap,status)

    
def removerSala():
    remover=str(input("Digite o codigo da sala: "))
    Sala.remover_sala(remover)

    
def opcao7():
    print (" \n \n ========= DESEJA EXCLUIR TODAS AS SALAS ?? ============\n")
    excluir_t=str(input("S ou N: "))
    if excluir_t == 'S' or excluir_t == 's':
        Sala.remover_todas_salas()
    else:
        return None

def opcao5():
    Sala.listar_salas()

def opcao2():
    status_ocp=str(input("Código da Sala que deseja alterar para Ocupada: "))
    Sala.definir_status_ocupada(status_ocp)
 
def opcao3():
    status_disp=str(input("Código da Sala que deseja alterar para Disponivel: "))
    Sala.definir_status_disponivel(status_disp)
