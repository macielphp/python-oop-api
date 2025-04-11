from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa
from db import criar_tabelas
from gui import App

if __name__ == '__main__':
    criar_tabelas()
    app = App()
    app.mainloop()