import unittest

import Filme

class TestConsulta(unittest.TestCase):
    def cadastrando_filme(self):
        codigo=Filme.cadastrar_filme('001','B13','1000min','Indicativa','Jose','Fox','Cartaz','Masculino')
        consulta=Filme.listar_filmes()
        self.assertEqual(1,len(consultas))
        self.assertEqual(1,codigo)
    
    def buscando_sala(self):
        codigo=Filme.cadastrar_filme('001','B13','1000min','Indicativa','Jose','Fox','Cartaz','Masculino')
        busca=Filme.buscar_filme('001')
        self.assertEqual(1,len(busca))
        self.assertEqual(1,codigo)
        
    def removendo_todas_salas(self):
        codigo=Filme.cadastrar_filme('001','B13','1000min','Indicativa','Jose','Fox','Cartaz','Masculino')        
        codigo2=Filme.cadastrar_filme('002','B13','1000min','Indicativa','Jose','Fox','Cartaz','Masculino')
        Filme.remover_todos_filmes()
        consulta = Filme.listar_filmes()
        self.assertEqual([], consulta)

if __name__== '__main__':
    unittest.main(exit=False)







    
