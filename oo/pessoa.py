class Pessoa:
    # metodo construtor da classe
    def __init__(self,*filhos, nome, idade=28):# atributos de classe
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    # metodo de classe
    def cumprimentar(self):
        return f'Ola mundo!!!{id(self)}'

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