class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)


carro = Carro("Toyota", "Corolla")
carro.exibir_info()