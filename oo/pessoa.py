class Pessoa:
    def __init__(self, nome=None, idade=30):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Diego')
    print(id(p))
    print(Pessoa.cumprimentar(p))
    # passagem da própria classe como parâmetro
    # é feita implicitamente pelo python
    print(p.cumprimentar())

    print(p.nome)
    p.nome = 'Aguiar'
    print(p.nome)