import unittest
import ControllerSala

class TestSala(unittest.TestCase):
    def setUp(self):
        ControllerSala.RemoverTodasSalas()

    def test_sem_sala(self):
        s = ControllerSala.ListarSala()
        self.assertEqual(0, len(s))
        
    def test_adicionar_sala(self):
        ControllerSala.AdicionarSala(1,"livre")
        s = ControllerSala.BuscarSala(1)
        self.assertEqual(2,len(s))
        self.assertEqual(1, s[0])
        self.assertEqual("livre", s[1])
        
    def test_buscar_sala(self):
        ControllerSala.AdicionarSala(1,"livre")
        
        a = ControllerSala.BuscarSala(1)
        self.assertEqual(1,a[0])
        self.assertEqual("livre",a[1])

        
    def test_buscar_sala(self):
        ControllerSala.AdicionarSala(1,"livre")
        ControllerSala.AdicionarSala(2,"ocupado")

        a = ControllerSala.ListarSala()
        a = len(a)
        self.assertEqual(2,a)

        
    def test_remover(self):
        ControllerSala.AdicionarSala(1,"livre")
        ControllerSala.RemoverSala(1)
        a = ControllerSala.BuscarSala(1)
        self.assertIsNone(a)
        
    def test_remover_todos(self):
        ControllerSala.AdicionarSala(1,"livre")
        ControllerSala.AdicionarSala(2,"ocupado")
        a = ControllerSala.RemoverTodasSalas()
        self.assertEqual([], a)
        
    def test_iniciar_sala(self):
        ControllerSala.IniciarSala()
        sala = ControllerSala.ListarSala()
        self.assertEqual(2, len(sala))

            
if __name__ == '__main__':
    unittest.main(exit=False)
