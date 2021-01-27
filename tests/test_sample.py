from unittest import TestCase

from src import my_module

#valores de comparação foram calculados manualmente
class Teste_funcoes_hoteis(TestCase):
    def test_lakewood(self):
        result = my_module.lakewood("Regular", ['mon', 'tues', 'wed'])
        self.assertEqual(result, 330)  

    def test_bridgewood(self):
        result = my_module.bridgewood("Regular", ['mon', 'tues', 'wed'])
        self.assertEqual(result, 480)
    
    def test_ridgewood(self):
        result = my_module.ridgewood("Regular", ['mon', 'tues', 'wed'])
        self.assertEqual(result, 660)