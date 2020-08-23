class Pessoa:
    def __init__(self,nome,idade,time):
        self.time = time
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Ola mundo!!!{id(self)}'

if __name__ == '__main__':
    p = Pessoa('King',28,'Cruzeiro')
    print(Pessoa .cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Julio'
    print(p.nome,p.idade,p.time)