"""
#teste
>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.velocidade
1
>>> motor.acelerar()
>>> motor.velocidade
2
>>> motor.acelerar()
>>> motor.velocidade
3
>>> motor.frear()
>>> motor.velocidade
1
>>> motor.frear()
>>> motor.velocidade
0
>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.girar_dir()
>>> direcao.valor
'Leste'
>>> direcao.girar_dir()
>>> direcao.valor
'Sul'
>>> direcao.girar_dir()
>>> direcao.valor
'Oeste'
>>> direcao.girar_dir()
>>> direcao.valor
'Norte'
>>> direcao.girar_esq()
>>> direcao.valor
'Oeste'
>>> direcao.girar_esq()
>>> direcao.valor
'Sul'
>>> direcao.girar_esq()
>>> direcao.valor
'Leste'
>>> direcao.girar_esq()
>>> direcao.valor
'Norte'
>>> carro = Carro(Direcao,Motor)
>>> carro.calcular_velocidade()
0
>>> carro.acelerar()
>>> carro.calcular_velocidade()
1
>>> carro.acelerar()
>>> carro.calcular_velocidade()
2
>>> carro.acelerar()
>>> carro.calcular_velocidade()
3
>>> carro.frear()
>>> carro.calcular_velocidade()
1
>>> carro.frear()
>>> carro.calcular_velocidade()
0

"""


class Motor:

    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade <= 1:
            self.velocidade = 0
        else:
            self.velocidade -= 2


class Direcao:

    def __init__(self):
        self.mov = ['Norte', 'Leste', 'Sul', 'Oeste']
        self.valor = self.mov[0]

    def girar_dir(self):
        if self.valor == self.mov[0]:
            self.valor = self.mov[1]
        elif self.valor == self.mov[1]:
            self.valor = self.mov[2]
        elif self.valor == self.mov[2]:
            self.valor = self.mov[3]
        else:
            self.valor = self.mov[0]

    def girar_esq(self):
        if self.valor == self.mov[3]:
            self.valor = self.mov[2]
        elif self.valor == self.mov[2]:
            self.valor = self.mov[1]
        elif self.valor == self.mov[1]:
            self.valor = self.mov[0]
        else:
            self.valor = self.mov[3]


class Carro:
    velocidade = 0
    def __init__(self,direcao,motor):
        self.direcao = direcao
        self.motor = motor




    def calcular_velocidade(self):
        return self.velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade <= 1:
            self.velocidade = 0
        else:
            self.velocidade -= 2



carro = Carro('Norte',0)
carro.acelerar()
carro.frear()