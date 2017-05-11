import unittest
import ControllerAtor

class TestAtor(unittest.TestCase):
    def setUp(self):
        ControllerAtor.RemoverTodosAtores()

    def test_sem_ator(self):
        atores = ControllerAtor.BuscarAtores()
        self.assertEqual(0, len(atores))
        
    def test_adicionar_ator(self):
        ControllerAtor.CadastrarAtor(2343,"Guilherme","Brasileiro",18)
        atores = ControllerAtor.BuscarAtor(2343)
        
        self.assertEqual(4,len(atores))
        self.assertEqual(2343, atores[0])

        self.assertEqual("Guilherme", atores[1])
        self.assertEqual("Brasileiro",atores[2])
        self.assertEqual(18,atores[3])
        
    def test_buscar_ator(self):
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
