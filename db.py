import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('cardapio.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS itens_cardapio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            categoria TEXT NOT NULL,
            tamanho TEXT,
            descricao TEXT
            
        )
    ''')

    conexao.commit()
    conexao.close()

def inserir_item(nome, preco, categoria, tamanho=None, descricao=None):
    conexao = sqlite3.connect('cardapio.db')
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO itens_cardapio (nome, preco, categoria, tamanho, descricao)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, preco, categoria, tamanho, descricao))

    conexao.commit()
    conexao.close()

def buscar_cardapio():
    conexao = sqlite3.connect('cardapio.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT nome, preco, categoria, tamanho, descricao FROM itens_cardapio')
    dados = cursor.fetchall()
    conexao.close()

    cardapio = []
    for item in dados:
        cardapio.append({
            "nome": item[0],
            "preco": item[1],
            "categoria": item[2],
            "tamanho": item[3],
            "descricao": item[4]
        })

    return cardapio

def deletar_item(nome):
    conexao = sqlite3.connect('cardapio.db')
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM itens_cardapio WHERE nome = ?', (nome,))
    conexao.commit()
    conexao.close()

