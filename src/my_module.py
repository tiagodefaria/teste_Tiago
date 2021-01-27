
# ---- função que encontra opção mais barata de hospedagem

def hospedagem(tipo, dias):
    lake = lakewood(tipo, dias)
    bridge = bridgewood(tipo, dias)
    ridge = ridgewood(tipo, dias)

    if lake > bridge:
        if bridge > ridge:
            print("Ridgewood")
        elif bridge < ridge:
            print("Bridgewood")
        else:
            print("Ridgewood")
    elif lake < bridge:
        if lake > ridge:
            print("Ridgewood")
        elif lake < ridge:
            print("Lakewood")
        else:
            print("Ridgewood")
    else:
        if lake > ridge:
            print("Ridgewood")
        elif lake < ridge:
            print("Bridgewood")
        else:
            print("Ridgewood")


#---- Lakewood
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


#---- Bridgewood
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


#---- Ridgewood
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


# --- módulo principal
if __name__ == '__main__':
    cliente = input()

    # separação da cadeia de caracteres
    cliente = cliente.split(':')
    tipo = cliente[0]
    datas = cliente[1]
    datas = datas.split(',')

    tamanho = len(datas)
    i = 0
    dias = []

    while (i < tamanho):
        aux = datas[i].split('(')
        aux = aux[1].replace(")", "")
        dias.append(aux)
        i += 1

    # ----- cálculo do preço da reserva
    hospedagem(tipo, dias)