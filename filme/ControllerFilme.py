filme = []

def CadastrarFilme(cod_filme,titulo,duracao,classi,diretor,distri,status,genero):
    aux = [cod_filme,titulo,duracao,classi,diretor,distri,status,genero]
    filme.append(aux)
    print ("=== Filme cadastrado === ")

def BuscarFilme(cod_filme):
    for f in filme:
        if (f[0] == cod_filme):
            print (f)
            return f
    return None

def ListarFilmes():
    global filme
    print (filme)
    return filme

def RemoverTodosFilmes():
    global filme
    filme = []
    print (" ==== Todos os filmes estão removido ==== ")
    return filme

def IniciarFilme():
    CadastrarFilme(1,"filme a","1:30","12","Eu","MeToo","Velho","comedia")
    CadastrarFilme(2,"filme b","1:10","16","Voce","MeToo","Velho","acao")
    
    

