class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor


class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []

    # Método para adicionar uma venda à lista de vendas da categoria
    def adicionar_venda(self, venda):
        if isinstance(venda, Venda):
            self.vendas.append(venda)
        else:
            print("Erro: O objeto não é uma instância da classe Venda.")

    # Método para calcular e retornar o total das vendas da categoria
    def total_vendas(self):
        total = sum(venda.quantidade * venda.valor for venda in self.vendas)
        return total


def main():
    categorias = []

    for i in range(2):  # Loop para criar 2 categorias
        nome_categoria = input("Digite o nome da categoria: ")
        categoria = Categoria(nome_categoria)

        for j in range(2):  # Loop para adicionar 2 vendas por categoria
            entrada_venda = input(
                f"Digite a venda {j+1} (produto, quantidade, valor) para {nome_categoria}: ")
            produto, quantidade, valor = entrada_venda.split(',')
            quantidade = int(quantidade.strip())
            valor = float(valor.strip())

            venda = Venda(produto.strip(), quantidade, valor)
            # Adiciona a venda à categoria
            categoria.adicionar_venda(venda)

        categorias.append(categoria)

    # Exibindo os totais de vendas para cada categoria
    for categoria in categorias:
        print(f"Vendas em {categoria.nome}: {categoria.total_vendas()}")


if __name__ == "__main__":
    main()
