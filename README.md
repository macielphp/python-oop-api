# 🍽️ Sistema de Restaurante com Interface Visual (CustomTkinter + SQLite)

Este é um sistema completo de gerenciamento de restaurantes com interface gráfica desenvolvida em Python usando [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) e banco de dados SQLite.

## 🧩 Funcionalidades

- Cadastrar restaurantes com:
  - Nome
  - Avaliação (de 1 a 10)
  - Estado (ativo/inativo)

- Cadastrar itens no cardápio:
  - Nome, Preço, Categoria (prato, bebida, sobremesa), Tamanho (opcional), Descrição (opcional)
  - Itens são vinculados a um restaurante selecionado

- Exibir e interagir com o cardápio:
  - Visualizar itens por restaurante
  - Editar itens do cardápio
  - Excluir itens

- Interface com navegação lateral simples e intuitiva

## 🖼️ Interface Gráfica

A interface foi construída com `CustomTkinter`, permitindo um visual moderno com temas claros e escuros, menus dropdown, campos de entrada personalizados, botões e mensagens de feedback.

## 🗃️ Banco de Dados

Utiliza SQLite como banco local:
- Tabela `restaurantes`: armazena os restaurantes cadastrados
- Tabela `cardapio`: armazena os itens vinculados a um restaurante

## 🚀 Como executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/sistema-restaurante.git
   cd sistema-restaurante
   ```

2. **Crie um ambiente virtual (opcional):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o projeto:**
   ```bash
   python gui.py
   ```

## 📦 Dependências

- Python 3.8+
- customtkinter

```bash
pip install customtkinter
```

## ✨ Futuras Melhorias

- Filtro por categoria no cardápio
- Exportação de dados para CSV
- Dashboard de estatísticas
- Sistema de login para múltiplos usuários

## 🧑‍💻 Autor

Feito com ❤️ por [Maciel Alves](https://github.com/macielphp)

---

Sinta-se à vontade para contribuir ou sugerir melhorias! 🚀
