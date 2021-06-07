import datetime
import math


class humanos(object):
    def __init__(self, nome, dtnasc, peso, altura: object):
        self.nome = nome
        self.dtnasc = dtnasc
        self.peso = peso
        self.altura = altura

    def getidade(self):
        calc = datetime.date.today() - self.dtnasc
        return int (calc.days/365.25)

    def getimc(self):
        return self.peso / math.pow(self.altura / 100., 2)


pessoa = humanos('Jorge', datetime.date(1985, 4, 1), 98, 178)
print(pessoa.nome)
print(pessoa.getidade, 'anos de idade')
print('IMC é de:', round(pessoa.getimc(), 2))
