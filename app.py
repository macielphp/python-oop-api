from database.db import criar_tabelas
from gui import App

if __name__ == '__main__':
    criar_tabelas()
    app = App()
    app.mainloop()