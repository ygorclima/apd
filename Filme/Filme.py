filmes=[]

def cadastrar_filme(cod_filme,titulo,duracao,classificacao,diretor,distribuidora,status,genero):
    filme=[cod_filme,titulo,duracao,classificacao,diretor,distribuidora,status,genero]
    filmes.append(filme)
    print (" \n \n ========= Cadastrado com Sucesso ============")
    
def buscar_filme(cod_filme):
     for i in filmes:
        if (i[0]== cod_filme):
            print (i)


def listar_filmes():
    for i in filmes:
        print(i)
        
def remover_todos_filmes():
    global filmes
    filmes=[]
    print(" \n \n ========= Excluído com Sucesso ============")
    return True
