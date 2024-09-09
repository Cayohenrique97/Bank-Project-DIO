class Bicicleta:

    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("fon fon")

    def parar(self):
        print("Parando a bicicleta ...")
        print("Bicicleta parada!")

    def trocar_marcha(self, nro_marcha):
        print("trocando marcha ...")

        def _trocar_marcha():
            if nro_marcha > self.marcha:
                print("Marcha trocada ....")
            else:
                print("Não foi possivel trocar de marcha ...")

    def correr(self):
        print("Vrummmm...")

#    def __str__(self) -> str:
        # Aqui colocamos na mao todos os atributos da classe, mas se mudar alguma coisa na classe terá que alterar manualmente.
 #       return f"Bicicleta: cor = {self.cor}, modelo = {self.modelo}, anor = {self.ano}, valor = {self.valor}"

    def __str__(self) -> str:
        # Aqui podemos retornar todos os atributos da classe de maneira automatica sem se preocupar com alterações na mesma
        return f"{self.__class__.__name__}: {'; '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()  # Bicicleta.buzinar(b1) mesma coisa
b1.parar()
b1.correr()
print(b1)

print(b1.modelo, b1.ano, b1.modelo)
