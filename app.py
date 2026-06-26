from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida


restarante_praca = Restaurante("praca", "gourmet")

bebida1 = Bebida("Coca-Cola", 5.0, "500ml")
bebida1.aplicar_desconto()  # Aplica o desconto de 5% na bebida
prato1 = Prato("Lasanha", 25.0, "Lasanha à bolonhesa")
prato1.aplicar_desconto()  # Aplica o desconto de 10% no prato
restarante_praca.adicionar_no_cardapio(bebida1)
restarante_praca.adicionar_no_cardapio(prato1)


def main():
    restarante_praca.exibir_cardapio

if __name__ == "__main__":
    main()