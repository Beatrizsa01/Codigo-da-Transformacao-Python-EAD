class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)


class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Autonomia da bateria:", self.autonomia_bateria, "km")


carro = CarroEletrico("Tesla", "Model 3", 500)
carro.exibir_info()