class Pessoa:
    def __init__(self,*filhos, nome, idade=28):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Ola mundo!!!{id(self)}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    julio = Pessoa(renzo,nome='Julio')
    print(julio.filhos)
    for filho in julio.filhos:
        print(filho.nome)