import unittest
import ControllerFilme

class TestFilme(unittest.TestCase):
    def setUp(self):
        ControllerFilme.RemoverTodosFilmes()

    def test_sem_filme(self):
        filmes = ControllerFilme.ListarFilmes()
        self.assertEqual(0,len(filmes))
                         
    def test_buscar_filme(self):
        ControllerFilme.CadastrarFilme(1,"filme a","1:30","12","Eu","MeToo","Velho","comedia")
        e = ControllerFilme.BuscarFilme(1)
        
        self.assertEqual(1,e[0])
        self.assertEqual("filme a",e[1])
        self.assertEqual("1:30",e[2])
        self.assertEqual("12",e[3])
        self.assertEqual("Eu",e[4])
        self.assertEqual("MeToo",e[5])
        self.assertEqual("Velho",e[6])
        self.assertEqual("comedia",e[7])

    def test_buscar(self):
        ControllerFilme.CadastrarFilme(1,"filme a","1:30","12","Eu","MeToo","Velho","comedia")
        ControllerFilme.CadastrarFilme(2,"filme b","1:10","16","Voce","MeToo","Velho","acao")
    
        
        e = ControllerFilme.ListarFilmes()
        e = len(e)
        self.assertEqual(2,e)
                         
    def test_remover_filme(self):
        ControllerFilme.CadastrarFilme(1,"filme a","1:30","12","Eu","MeToo","Velho","comedia")
        
        ControllerFilme.RemoverTodosFilmes()
        
        e = ControllerFilme.BuscarFilme(1)
        self.assertIsNone(e)

    def test_iniciar_elenco(self):
        ControllerFilme.IniciarFilme()
        e = ControllerFilme.ListarFilmes()
        self.assertEqual(2, len(e))
        
if __name__ == '__main__':
    unittest.main(exit=False)
