import unittest
import ControllerIngresso

class TestIngresso(unittest.TestCase):
    def setUp(self):
        ControllerIngresso.RemoverTodosIngresso()

    def test_sem_ingresso(self):
        ingresso = ControllerIngresso.ListarIngresso()
        self.assertIsNone(ingresso)
                         
    def test_buscar_ingresso(self):
        ControllerIngresso.Ingresso(1)
        e = ControllerIngresso.BuscaIngresso(1)
        self.assertEqual(1,e[0])
        self.assertEqual("inteiro",e[1])
                         
    def test_remover(self):
        ControllerIngresso.Ingresso(1)
        ControllerIngresso.RemoverIngresso(1)
        e = ControllerIngresso.BuscaIngresso(1)
        self.assertIsNone(e)
        

    def test_remover_todos(self):
        ControllerIngresso.Ingresso(1)
        ControllerIngresso.Ingresso(1)
        e = ControllerIngresso.RemoverTodosIngresso()
        self.assertEqual([],e)

        
if __name__ == '__main__':
    unittest.main(exit=False)
