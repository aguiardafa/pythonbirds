class Pessoa:
    def __init__(self, *filhos, nome=None, idade=30):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa(nome='Diego')
    print(id(p))
    print(Pessoa.cumprimentar(p))
    # passagem da própria classe como parâmetro
    # é feita implicitamente pelo python
    print(p.cumprimentar())

    # manipulando atributos de instancia
    print(p.nome)
    p.nome = 'Aguiar'
    print(p.nome)

    # manipulando atributos complexos
    diego = p
    juarez = Pessoa(diego, nome='Juarez')
    print(juarez.nome)
    for filho in juarez.filhos:
        print(filho.nome)

    # manipulando atributos dinamicos
    juarez.sobrenome = 'Aguiar'
    print(juarez.sobrenome)
    print(juarez.__dict__)
    print(diego.__dict__)
    del diego.filhos
    print(diego.__dict__)