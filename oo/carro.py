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
>>> carro = Carro(direcao,motor)
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
# classe motor
class Motor:

    # velocidade inicial == 0
    def __init__(self):
        self.velocidade = 0

    # acrescenta em 1 a velocidade
    def acelerar(self):
        self.velocidade += 1

    # frear reduz a velocidade em 2,mas o menor valor possivel é 0
    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0,self.velocidade) #funçao MAX(0,self.vel) 0 e o maximo q pode chegar

# criando constante comforme a pep sempre sendo td maiúscula
NORTE ='Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

# classe Direção
class Direcao:

    # dicionario com rotaçao dir e esq
    rotacao_direita_dic = {NORTE:LESTE ,LESTE:SUL ,SUL:OESTE,OESTE:NORTE}
    rotacao_esquerda_dic = {NORTE:OESTE ,OESTE:SUL,SUL:LESTE, LESTE:NORTE }

    def __init__(self):
        self.valor = NORTE

    def girar_dir(self):
      self.valor = self.rotacao_direita_dic[self.valor]
    def girar_esq(self):
       self.valor =self.rotacao_esquerda_dic[self.valor]

class Carro:

    def __init__(self,direcao,motor):
        self.velocidade = 0

    def calcular_velocidade(self):
        return self.velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade <=1:
            self.velocidade = 0
        else:
            self.velocidade -= 2


