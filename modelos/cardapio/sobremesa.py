from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho, descricao):
        super().__init__(nome, preco)
        self.tipo = tipo
        self.tamanho = tamanho
        self.descricao = descricao  

    def __str__(self):
        return f"Tipo: {self._tipo} | Tamanho: {self._tamanho} | descricao: {self._descricao}"

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.15)