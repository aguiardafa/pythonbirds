class Pessoa:
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(id(p))
    print(Pessoa.cumprimentar(p))
    # passagem da própria classe como parâmetro
    # é feita implicitamente pelo python
    print(p.cumprimentar())