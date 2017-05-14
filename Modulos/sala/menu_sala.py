from sala import controller_altera

def ShowMenu():
    print ('\n 1 - Adiciona Sala: \n','2 - Definir status ocupado: \n',
           '3 - Definir status livre: \n','4 - Buscar sala: \n',
           '5 - Listar salas: \n','6 - Remover salas: \n','7 - Remover todas as salas: \n','0 - Encerrar: \n')
    escolhe=int(input('Escolha: '))
    if escolhe == 1:
        controller_altera.opcao1()
    elif escolhe == 2:
        controller_altera.opcao2()
    elif escolhe == 3:
        controller_altera.opcao3()
    elif escolhe == 4:
        controller_altera.opcao4()
    elif escolhe == 5:
        controller_altera.opcao5()
    elif escolhe == 6:
        controller_altera.removerSala()
    elif escolhe == 7:
        controller_altera.opcao7()
    elif escolhe == 0:
        return (escolhe)
        
