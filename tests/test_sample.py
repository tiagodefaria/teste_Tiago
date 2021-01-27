from unittest import TestCase

#!-- funções utilizadas no código

def lakewood(tipo, dias):
    if tipo == "Regular":
        preco = 0
        i = 0
        while (i < len(dias)):
            if dias[i] == "sat" or dias[i] == "sun":
                preco += 90
            elif dias[i] == "mon" or dias[i] == "tues" or dias[i] == "wed" or dias[i] == "thur" or dias[i] == "fri":
                preco += 110
            else:
                print(dias[i], " -> não é um dia da semana válido e será desconsiderado")
            i += 1
        return preco
    elif tipo == "Reward":
        preco = 0
        i = 0
        while (i < len(dias)):
            if dias[i] == "sat" or dias[i] == "sun":
                preco += 80
            elif dias[i] == "mon" or dias[i] == "tues" or dias[i] == "wed" or dias[i] == "thur" or dias[i] == "fri":
                preco += 80
            else:
                print(dias[i], " -> não é um dia da semana válido e será desconsiderado")
            i += 1
        return preco
    else:
        print("ERRO")
        exit()

def bridgewood(tipo, dias):
    if tipo == "Regular":
        preco = 0
        i = 0
        while (i < len(dias)):
            if dias[i] == "sat" or dias[i] == "sun":
                preco += 60
            elif dias[i] == "mon" or dias[i] == "tues" or dias[i] == "wed" or dias[i] == "thur" or dias[i] == "fri":
                preco += 160
            else:
                print(dias[i], " -> não é um dia da semana válido e será desconsiderado")
            i += 1
        return preco
    elif tipo == "Reward":
        preco = 0
        i = 0
        while (i < len(dias)):
            if dias[i] == "sat" or dias[i] == "sun":
                preco += 50
            elif dias[i] == "mon" or dias[i] == "tues" or dias[i] == "wed" or dias[i] == "thur" or dias[i] == "fri":
                preco += 110
            else:
                print(dias[i], " -> não é um dia da semana válido e será desconsiderado")
            i += 1
        return preco
    else:
        print("ERRO")
        exit()

def ridgewood(tipo, dias):
    if tipo == "Regular":
        preco = 0
        i = 0
        while (i < len(dias)):
            if dias[i] == "sat" or dias[i] == "sun":
                preco += 150
            elif dias[i] == "mon" or dias[i] == "tues" or dias[i] == "wed" or dias[i] == "thur" or dias[i] == "fri":
                preco += 220
            else:
                print(dias[i], " -> não é um dia da semana válido e será desconsiderado")
            i += 1
        return preco
    elif tipo == "Reward":
        preco = 0
        i = 0
        while (i < len(dias)):
            if dias[i] == "sat" or dias[i] == "sun":
                preco += 40
            elif dias[i] == "mon" or dias[i] == "tues" or dias[i] == "wed" or dias[i] == "thur" or dias[i] == "fri":
                preco += 100
            else:
                print(dias[i], " -> não é um dia da semana válido e será desconsiderado")
            i += 1
        return preco
    else:
        print("ERRO")
        exit()

#valores de comparação foram calculados manualmente
class Teste_funcoes_hoteis(TestCase):
    def test_lakewood(self):
        result = lakewood("Regular", ['mon', 'tues', 'wed'])
        self.assertEqual(result, 330)  

    def test_bridgewood(self):
        result = bridgewood("Regular", ['mon', 'tues', 'wed'])
        self.assertEqual(result, 480)
    
    def test_ridgewood(self):
        result = ridgewood("Regular", ['mon', 'tues', 'wed'])
        self.assertEqual(result, 660)