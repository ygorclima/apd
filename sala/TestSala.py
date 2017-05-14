import unittest
import ControllerSala

class TestSala(unittest.TestCase):
    def setUp(self):
        ControllerSala.RemoverTodasSalas()

    def test_sem_sessao(self):
        s = ControllerAtor.ListarSala()
        self.assertEqual(0, len(s))
        
    def test_adicionar_sessao(self):
        ControllerSala.AdicionarSala(1,"livre")
        s = ControllerSala.BuscarSala(1)
        
        self.assertEqual(1,len(atores))
        self.assertEqual(1, s[0])
        self.assertEqual("livre", s[1])

        
    def test_buscar_ator(self):
        ControllerSala.AdicionarSala(1,"
        ControllerAtor.CadastrarAtor(1,"Messias","Brasileiro",21)
        a = ControllerAtor.BuscarAtor(1)
        self.assertEqual(1,a[0])
        self.assertEqual("Messias",a[1])
        self.assertEqual("Brasileiro",a[2])
        self.assertEqual(21,a[3])
    def test_buscar_atores(self):
        ControllerAtor.CadastrarAtor(1,"Messias","Brasileiro",21)
        ControllerAtor.CadastrarAtor(2,"Teste","Brasileiro",1)
        a = ControllerAtor.BuscarAtores()
        
    def test_remover_ator(self):
        ControllerAtor.CadastrarAtor("1","Messias","Brasileiro",21)
        ControllerAtor.RemoverAtor(1)
        a = ControllerAtor.BuscarAtor(1)
        self.assertIsNone(a)
        
    def test_remover_todos_atores(self):
        ControllerAtor.CadastrarAtor(1,"Messias","Brasileiro",21)
        ControllerAtor.CadastrarAtor(2,"Teste","Brasileiro",1)
        a = ControllerAtor.RemoverTodosAtores()
        self.assertEqual([], a)
        
    def test_iniciar_atores(self):
        ControllerAtor.IniciarAtores()
        atores = ControllerAtor.BuscarAtores()
        self.assertEqual(3, len(atores))

            
if __name__ == '__main__':
    unittest.main(exit=False)
