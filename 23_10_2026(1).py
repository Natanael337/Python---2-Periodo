#Criação de Classe
class Carro:
#Inicializando a Atributos do Carro através de seu Método de Construção
    def __init__(self, fabricante, modelo, ano):
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
    #Sistema de Ligar e Desligar
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False
    def status_do_carro(self):
        if self.ligado:
            print('O Carro {} está Ligado!'.format(self.modelo))
        else:
            print('O Carro {} está Desligado!'.format(self.modelo))

#Criação de Objetos
meu_carro = Carro('Renault','Sandero', 2020)
carro_do_meu_amigo = Carro('Ford', 'Fusion', 2015)

#Printando Características do Meu Carro
print(meu_carro.fabricante)
print(meu_carro.ano)

#Printando Características do Carro do Meu Amigo
print(carro_do_meu_amigo.fabricante)
print(carro_do_meu_amigo.ano)

meu_carro.ligar()
meu_carro.status_do_carro()
carro_do_meu_amigo.status_do_carro()
