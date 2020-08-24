class Pessoa:
    # atribudo default ou atributo de classe
    olhos = 2

    # metodo construtor da classe
    def __init__(self,*filhos, nome, idade=28):# atributos de classe
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    # metodo
    def cumprimentar(self):
        return f'Ola mundo!!!{id(self)}'

    # metodo de classe()
    @staticmethod# <-- decoreitor
    def

# metodo main ->> qdo importar esse pagina apenas execultara od metodos.
if __name__ == '__main__':

    # instanciando as pessoas
    renzo = Pessoa(nome='Renzo')
    julio = Pessoa(renzo,nome='Julio')

    print(julio.filhos)

    for filho in julio.filhos:
        print(filho.nome)
        print(id(filho))

    # atribuinado dinamicamente um atributo no objeto julio(apenas nesse objeto)
    julio.sobrenome = 'Cesar'
    print(julio.sobrenome)

    # acessando tdos os atributos dos objetos
    print(julio.__dict__)
    print(renzo.__dict__)

    # removendo algum atributo dinamicamente pelo comando del
    del renzo.idade

    # acessando tdos os atributos dos objetos
    print(julio.__dict__)
    print(renzo.__dict__)

    # acessando atributo de classe(ele e acesando pela classe)
    print(Pessoa.olhos)

    # acessando o atributo de classe(pelo objeto)
    print(julio.olhos)
    print(renzo.olhos)

    # ID da classe e do objeto e o mesmo idenpedente de onde ele e acessado
    print(id(Pessoa.olhos),id(julio.olhos),id(renzo.olhos))# mesmo valor de id(pois esta sendo instanciado  na classe)

    # ao mudar o atributo de classe usdabndo um atributo dinamico vc altera a id do objeto em que esta sendo instanciado.
    renzo.olhos = 1

    # ID da classe e do objeto e o mesmo idenpedente de onde ele e acessado
    print(id(Pessoa.olhos),id(julio.olhos),id(renzo.olhos)) # id de renzo mudou pq foi "instaciado dinamicamente"
