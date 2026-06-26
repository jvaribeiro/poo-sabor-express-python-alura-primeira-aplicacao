from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []
    cardapio = []

    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Restaurante: {self.nome} | Categoria: {self.categoria} | Ativo: {self.ativo}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'Nome'.ljust(30) + f'| Categoria'.ljust(30) + f'| Ativo'.ljust(30) + f'| Avaliações'.ljust(30))
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome}'.ljust(30) + f'| {restaurante.categoria}'.ljust(30) + f'| {restaurante.ativo}'.ljust(30) + f'| {restaurante.media_avaliacoes}'.ljust(30))
        
    @property
    def ativo(self):
        return 'Ativado' if self._ativo else 'Desativado'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
        
    def receber_avaliacao(self, cliente, nota):
        if nota >= 0 and nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

        
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Sem avaliações'
        total = sum(avaliacao._nota for avaliacao in self._avaliacao)
        return round(total / len(self._avaliacao), 1)
    
    # def adicionar_bebida_cardapio(self, bebida):
    #     self._cardapio.append(bebida)

    # def adicionar_prato_cardapio(self, prato):
    #     self._cardapio.append(prato)
        
    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardápio do Restaurante {self.nome}:')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, '_descricao'):
                print(f'{i}. Nome: {item._nome} | Preço: R${item._preco:.2f} | Descrição: {item._descricao}')
            elif hasattr(item, '_tamanho'):
                print(f'{i}. Nome: {item._nome} | Preço: R${item._preco:.2f} | Tamanho: {item._tamanho}')