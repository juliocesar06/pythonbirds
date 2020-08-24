
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

