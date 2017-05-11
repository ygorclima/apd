import Controller_filme

while 1==1:
    print ('\n 1 - Adiciona Filme: \n','2 - Buscar Filme: \n',
           '3 - Listar Filmes: \n','4 - Remover todas as salas: \n','0 - Encerrar: \n')
    escolhe=int(input('Escolha: '))
    if escolhe == 1:
        Controller_filme.opcao1()
    elif escolhe == 2:
        Controller_filme.opcao2()
    elif escolhe == 3:
        Controller_filme.opcao3()
    elif escolhe == 4:
        Controller_filme.opcao4()
    elif escolhe == 0:
        break
