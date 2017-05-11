import unittest
import ControllerElenco

class TestElenco(unittest.TestCase):
    def setUp(self):
        ControllerElenco.RemoverTodosElenco()

    def test_sem_ator(self):
        elencos = ControllerElenco.BuscarTodosElenco()
        print (elencos)
        self.assertEqual(0,len(elencos))
                         
    def test_buscar_ator_filme(self):
        ControllerElenco.AdicionarAtor(1,1,1,"coadjuvante")
        e = ControllerElenco.BuscarElenco(1)
        self.assertEqual(1,e[0])
        self.assertEqual(1,e[1])
        self.assertEqual(1,e[2])
        self.assertEqual("coadjuvante",e[3])

    def test_buscar_elenco(self):
        ControllerElenco.AdicionarAtor(1,1,1,"coadjuvante")
        e = ControllerElenco.BuscarElenco(1)
        self.assertEqual(1,e[0])
        self.assertEqual(1,e[1])
        self.assertEqual(1,e[2])
        self.assertEqual("coadjuvante",e[3])

    def test_buscar_elenco_filme(self):
        ControllerElenco.AdicionarAtor(1,1,1,"coadjuvante")
        e = ControllerElenco.BuscarElencoFilme(1)
        self.assertEqual(1,e[0])
        self.assertEqual(1,e[1])
        self.assertEqual(1,e[2])
        self.assertEqual("coadjuvante",e[3])
                         
    def test_remover_elenco(self):
        ControllerElenco.AdicionarAtor(1,1,1,"Coadjuvante")
        ControllerElenco.RemoverElenco(1)
        e = ControllerElenco.BuscarElenco(1)
        self.assertIsNone(e)

    def test_remover_todos_elenco(self):
        ControllerElenco.AdicionarAtor(1,1,1,"Coadjuvante")
        ControllerElenco.AdicionarAtor(1,1,1,"Principal")
        e = ControllerElenco.RemoverTodosElenco()
        self.assertEqual([],e)
        
    def test_iniciar_elenco(self):
        ControllerElenco.IniciarElenco()
        e = ControllerElenco.BuscarTodosElenco()
        self.assertEqual(2, len(e))
        
if __name__ == '__main__':
    unittest.main(exit=False)
