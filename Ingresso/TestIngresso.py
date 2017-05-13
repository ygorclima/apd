import unittest
import ControllerIngresso

class TestElenco(unittest.TestCase):
    def setUp(self):
        ControllerIngresso.RemoverTodosIngresso()

    def test_sem_ingresso(self):
        ingresso = ControllerIngresso.ListarIngresso()
        print ("aqui",ingresso)
        self.assertEqual(0,len(ingresso))
                         
    def test_buscar_ingresso(self):
        ControllerIngresso.Ingresso(1)
        e = ControllerIngresso.BuscaIngresso(1)
        self.assertEqual(1,e[0])
                         
    def test_remover(self):
        ControllerIngresso.Ingresso(1)
        ControllerjIngresso.RemoverIngresso(1)
        e = ControllerIngresso.BuscarIngresso(1)
        self.assertIsNone(e)

    def test_remover_todos(self):
        ControllerIngresso.Ingresso(1)
        ControllerIngresso.Ingresso(1)
        e = ControllerIngresso.RemoverTodosIngresso()
        self.assertEqual([],e)
        
    def test_iniciar_elenco(self):
        ControllerIngresso.IniciarIngresso()
        e = ControllerIngresso.BuscarTodosIngresso()
        self.assertEqual(2, len(e))
        
if __name__ == '__main__':
    unittest.main(exit=False)
