class veiculo():
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("ligando motor...")


class motocicleta(veiculo):
    pass


class carro(veiculo):
    pass


class caminhao(veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_Carregado(self):
        print(f"{'Sim,' if self.carregado else 'Não,'} estou carregado")

    def __str__(self) -> str:
        # Aqui podemos retornar todos os atributos da classe de maneira automatica sem se preocupar com alterações na mesma
        return f"{self.__class__.__name__}: {'; '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


moto = motocicleta("vermelha", "AAA-0000", 2)
moto.ligar_motor()
caminhao = caminhao("roxo", "xde-0098", 8, True)
caminhao.esta_Carregado()
print(caminhao)
