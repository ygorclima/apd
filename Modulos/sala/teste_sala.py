import unittest

import Sala

class TestConsulta(unittest.TestCase):

    def adicionando_sala(self):
        codigo=Sala.adicionar_sala('001',100,'Ocupada')
        consulta=Sala.listar_salas()
        self.assertEqual(1,len(consultas))
        self.assertEqual(1,codigo)
    
    def buscando_sala(self):
        codigo=Sala.adicionar_sala('001',100,'Ocupada')
        busca=Sala.buscar_sala('001')
        self.assertEqual(1,len(busca))
        self.assertEqual(1,codigo)
   
    def remover_sala(self):
        Sala.adicionar_sala("003", 100, 'Ocupada')
        Sala.remover_sala('003')
        consulta = Sala.listar_salas()
        self.assertEqual([], consulta)
        
    def removendo_todas_salas(self):
        Sala.adicionar_sala("003", 100, 'Ocupada')
        Sala.adicionar_sala("004", 200, 'Disponivel')         
        Sala.remover_todas_salas()
        consulta = Sala.listar_salas()
        self.assertEqual([], consulta)

    def definindo_status_ocupada(self):
        cons=Sala.adicionar_sala("003", 100, 'Ocupada')
        Sala.definir_status_ocupada('003')
        self.assertEqual('Ocupado', cons[2])
    
    def definindo_status_disponivel(self): 
        cons=Sala.adicionar_sala("003", 100, 'Disponivel')
        Sala.definir_status_ocupada('003')
        self.assertEqual('Disponivel', cons[2])


if __name__== '__main__':
    unittest.main(exit=False)







    
