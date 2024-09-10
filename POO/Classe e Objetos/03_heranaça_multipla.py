class Animal:

    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self) -> str:
        # Aqui podemos retornar todos os atributos da classe de maneira automatica sem se preocupar com alterações na mesma
        return f"{self.__class__.__name__}: {'; '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico


class Cachorro(Mamifero):
    pass


class Gato(Mamifero):
    pass


class Leao(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    pass


gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)

Ornitorrinco = Ornitorrinco(
    nro_patas=4, cor_pelo="Vermelho", cor_bico="Laranja")
print(Ornitorrinco)


class Foo:
    def hello(self):
        print(self.__class__.__name__.lower())


class Bar(Foo):
    def hello(self):
        return super().hello()


bar = Bar()

bar.hello()
