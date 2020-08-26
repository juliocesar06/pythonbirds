import random
class Carro:
    # atribuiçao da classe velocidade
    velocidade = 0

    def __init__(self):
        pass

class Motor(Carro):


    # adciciona 1 ponto na velocidade
    def acelerar(self):
        Carro.velocidade += 1

    # funçao retira 2 pontos de velocidade, se velocidade for <=1 ,entao velocidade = 0
    def frear(self):

        if Carro.velocidade <=1:
            Carro.velocidade = 0
        else:
            Carro.velocidade -= 2

class Direcao(Carro):
    lado = ['Norte','Leste','Sul','Oeste',]
    status = 0

    def direcao(self):
        return Direcao.lado[Direcao.status]

    def girar_dir(self):

        if Direcao.status == Direcao.lado[0]:
            Direcao.status = Direcao.lado[1]

        elif Direcao.status == Direcao.lado[1]:
            Direcao.status = Direcao.lado[2]

        elif Direcao.status == Direcao.lado[2]:
            Direcao.status = Direcao.lado[3]
        else:
            Direcao.status = Direcao.lado[0]
        return Direcao.status

    def girar_esq(self):

        if Direcao.status == Direcao.lado[0]:
            Direcao.status = Direcao.lado[3]

        elif Direcao.status == Direcao.lado[1]:
            Direcao.status = Direcao.lado[2]

        elif Direcao.status == Direcao.lado[2]:
            Direcao.status = Direcao.lado[1]

        else:
            Direcao.status = Direcao.lado[0]


motor = Motor()
print(motor.velocidade)#0
motor.acelerar()
print(motor.velocidade)#1
motor.acelerar()
print(motor.velocidade)#2
motor.acelerar()
print(motor.velocidade)#3
motor.frear()
print(motor.velocidade)#1
motor.frear()
print(motor.velocidade)#0

direcao = Direcao()
count = 0
c = 0
for i in range(1,5):
    x = random.randint(0,1)
    if x == 1:
        direcao.girar_dir()
        print(direcao.status)
        print(' -->')
        count += 1

    else:
        direcao.girar_esq()
        print(direcao.status)
        print(' <--')
        c += 1
print(f' foram {count} a dir e {c} a esquerda')