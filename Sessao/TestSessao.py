import unittest
import ControllerSessao

class TestSessao(unittest.TestCase):
    def setUp(self):
        ControllerSessao.RemoverTodosSessao()

    def test_sem_sessao(self):
        s = ControllerSessao.ListarSessao()
        self.assertEqual(0, len(s))
        
    def test_adicionar_sessao(self):
        ControllerSessao.CriarSessao(1,1,1,"8:30")
        s = ControllerSessao.ListarSessao()
        self.assertEqual(1,len(s))
        
        self.assertEqual([1, 1, 1, '8:30'], s[0])
       
        
    def test_buscar_sessao(self):
        ControllerSessao.IniciarSessao()
        
        a = ControllerSessao.ListarSessao()
        a = len(a)
        self.assertEqual(2,a)
        
    def test_remover(self):
        ControllerSessao.CriarSessao(1,1,1,"8h30")
        a = ControllerSessao.RemoverSessao(1)
        self.assertEqual(True,a)
   
    def test_iniciar_sessao(self):
        ControllerSessao.IniciarSessao()
        s = ControllerSessao.ListarSessao()
        self.assertEqual(2, len(s))

            
if __name__ == '__main__':
    unittest.main(exit=False)
