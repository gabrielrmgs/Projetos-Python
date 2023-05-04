'''
testando
'''


class carro:
    
    def __init__(self, marca, ano, motor):
        self.marca = marca
        self.ano = ano
        self.motor = motor

    def IniciarCarro(self):
        print("ligando carro")
        print(f"{self.marca} iniciado")

    def IformacoesCarro(self):
        print(self.marca, self.ano, self.motor)


carro1 = carro('pegeut', 2010, 2.0)
carro2 = carro('civ',2000,1.5)
carro3 = carro('hond',2020,3.0)
carro1.IformacoesCarro()

carro1.IniciarCarro()

carro2.IniciarCarro()
