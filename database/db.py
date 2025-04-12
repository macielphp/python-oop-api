import sqlite3

def conectar():
    return sqlite3.connect('restaurantes.db')

def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    # Criar tabela de restaurantes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS restaurantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            avaliacao INTEGER CHECK(avaliacao BETWEEN 1 AND 10),
            estado TEXT CHECK(estado IN ('ativo', 'inativo')) NOT NULL
        )
    ''')

    # Criar nova tabela de itens_cardapio com restaurante_id
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS itens_cardapio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            categoria TEXT NOT NULL,
            tamanho TEXT,
            descricao TEXT,
            restaurante_id INTEGER NOT NULL,
            FOREIGN KEY (restaurante_id) REFERENCES restaurantes(id)
        )
    ''')

    conexao.commit()
    conexao.close()


def inserir_item(nome, preco, categoria, tamanho, descricao, restaurante_id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO itens_cardapio (nome, preco, categoria, tamanho, descricao, restaurante_id)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nome, preco, categoria, tamanho, descricao, restaurante_id))

    conexao.commit()
    conexao.close()

def buscar_restaurantes_ativos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome FROM restaurantes WHERE estado = 'ativo'")
    dados = cursor.fetchall()
    conexao.close()
    return dados

def buscar_cardapio_por_restaurante(restaurante_id):
    conexao = conectar()
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM itens_cardapio WHERE restaurante_id = ?", (restaurante_id,))
    dados = cursor.fetchall()
    conexao.close()
    return [dict(row) for row in dados]

def deletar_item(item_id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM itens_cardapio WHERE id = ?", (item_id,))
    conexao.commit()
    conexao.close()

def editar_item(id_item, nome, preco, categoria, tamanho, descricao):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE itens_cardapio
        SET nome = ?, preco = ?, categoria = ?, tamanho = ?, descricao = ?
        WHERE id = ?
    ''', (nome, preco, categoria, tamanho, descricao, id_item))

    conexao.commit()
    conexao.close()

def inserir_restaurante(nome, avaliacao, estado):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO restaurantes (nome, avaliacao, estado)
        VALUES (?, ?, ?)
    ''', (nome, avaliacao, estado))
    conexao.commit()
    conexao.close()