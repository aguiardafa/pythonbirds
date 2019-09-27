class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=30):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    pass


class Mutante(Pessoa):
    olhos = 3  # sobrescrita de atributo de classe


if __name__ == '__main__':
    p = Homem(nome='Diego')  # utilizando herença
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

    # atributo de classe (atributos default)
    print(Pessoa.olhos)  # acessando diretamente pela class
    print(juarez.olhos)  # acessando pelo objeto
    print(diego.olhos)
    print(id(Pessoa.olhos), id(juarez.olhos), id(diego.olhos))
    diego.olhos = 1
    print(diego.__dict__)
    print(id(Pessoa.olhos), id(juarez.olhos), id(diego.olhos))
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(juarez.olhos)
    print(diego.olhos)
    del diego.olhos
    print(Pessoa.olhos)
    print(juarez.olhos)
    print(diego.olhos)
    Pessoa.olhos = 2

    # metodos de classe (utilizando decoreitor @)
    # acessando diretamente pela classe e pelo objeto
    print(Pessoa.metodo_estatico(), diego.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), diego.nome_e_atributos_de_classe())

    # trabalhando com herança
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(diego, Pessoa))
    print(isinstance(diego, Homem))

    mutante = Mutante('TesteMutante')
    print(diego.olhos)
    print(mutante.olhos)

