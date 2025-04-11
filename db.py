import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('cardapio.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS itens_cardapio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            tamanho TEXT,
            descricao TEXT
        )
    ''')

    conexao.commit()
    conexao.close()

def inserir_item(nome, preco, tamanho=None, descricao=None):
    conexao = sqlite3.connect('cardapio.db')
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO itens_cardapio (nome, preco, tamanho, descricao)
        VALUES (?, ?, ?, ?)
    ''', (nome, preco, tamanho, descricao))

    conexao.commit()
    conexao.close()

def buscar_cardapio():
    conexao = sqlite3.connect('cardapio.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT nome, preco, tamanho, descricao FROM itens_cardapio')
    dados = cursor.fetchall()
    conexao.close()

    cardapio = []
    for item in dados:
        cardapio.append({
            "nome": item[0],
            "preco": item[1],
            "tamanho": item[2],
            "descricao": item[3]
        })

    return cardapio