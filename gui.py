import customtkinter as ctk


ctk.set_appearance_mode('light') # 'Dark', "Light", "System";
ctk.set_default_color_theme('blue') # Pode usar: "blue", "green", "dark-blue";

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Sistema de Restaurante')
        self.geometry('800x500')

        # Layout Principal
        self.grid_columnconfigure(1, weight=1)

        # ============== NAV LATERAL ==================
        self.nav_frame = ctk.CTkFrame(self, width=200)
        self.nav_frame.grid(row=0, column=0, sticky="ns")
        self.nav_frame.grid_propagate(False)

        ctk.CTkLabel(self.nav_frame, text="Menu", font=("Arial", 20)).pack(pady=10)

        self.btn_inicio = ctk.CTkButton(self.nav_frame, text="Início", command=self.mostrar_inicio)
        self.btn_inicio.pack(pady=5)

        self.btn_restaurantes = ctk.CTkButton(self.nav_frame, text="Restaurantes", command=self.mostrar_restaurantes)
        self.btn_restaurantes.pack(pady=5)

        self.btn_cadastrar = ctk.CTkButton(self.nav_frame, text="Cadastrar", command=self.mostrar_cadastro)
        self.btn_cadastrar.pack(pady=5)

        self.btn_avaliacoes = ctk.CTkButton(self.nav_frame, text="Avaliações", command=self.mostrar_avaliacoes)
        self.btn_avaliacoes.pack(pady=5)

        # ==========Área de conteúdo==================
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.label_conteudo = ctk.CTkLabel(self.main_frame, text='Bem-vindo(a)!', font=("Arial", 24))
        self.label_conteudo.pack(pady=50)

    def mostrar_inicio(self):
        self._atualizar_conteudo_cardapio()

    def mostrar_restaurantes(self):
        self._atualizar_conteudo("Página de restaurantes")

    def mostrar_cadastro(self):

        for widget in self.main_frame.winfo_children():
            widget.destroy()

        ctk.CTkLabel(self.main_frame, text="Cadastrar Novo Item", font=("Arial", 20)).pack(pady=20)

        nome_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Nome do item")
        nome_entry.pack(pady=5)
        
        preco_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Preço(ex: 9.99)")
        preco_entry.pack(pady=5)
        
        categoria_menu = ctk.CTkOptionMenu(self.main_frame, values=["bebidas", "prato", "sobremesa"])
        categoria_menu.set("bebida") #Valor padrão
        categoria_menu.pack(pady=5)

        tamanho_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Tamanho (opcional)")
        tamanho_entry.pack(pady=5)

        descricao_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Descrição(opcional)")
        descricao_entry.pack(pady=5)

        resultado_label = ctk.CTkLabel(self.main_frame, text="")
        resultado_label.pack(pady=5)

        def cadastrar():
            nome = nome_entry.get()
            preco = preco_entry.get()
            categoria = categoria_menu.get()
            tamanho = tamanho_entry.get()
            descricao = descricao_entry.get()

            if not nome or not preco or not categoria:
                resultado_label.configure(text="Nome, preço e categorias são obrigatórios!", text_color="red")
                return

            try:
                preco = float(preco)
            except ValueError:  
                resultado_label.configure(text="Preço inválido!", text_color="red")
                return
            from db import inserir_item
            inserir_item(nome, preco, categoria,tamanho if tamanho else None, descricao if descricao else None)

            resultado_label.configure(text="Item cadastrado com sucesso!", text_color="green")

            # Limpar os campos
            nome_entry.delete(0, "end")
            preco_entry.delete(0, "end")
            categoria_menu.set("bebida")
            tamanho_entry.delete(0, "end")
            descricao_entry.delete(0, "end")

        ctk.CTkButton(self.main_frame, text="Cadastrar", command=cadastrar).pack(pady=10)

    def mostrar_avaliacoes(self):
        self._atualizar_conteudo("Página de avaliações")

    def _atualizar_conteudo(self, texto):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        ctk.CTkLabel(self.main_frame, text=texto, font=("Arial", 20)).pack(pady=50)

    def _atualizar_conteudo_cardapio(self):
        from db import buscar_cardapio

        for widget in self.main_frame.winfo_children():
            widget.destroy()

        ctk.CTkLabel(self.main_frame, text="Cardápio do Restaurante Praça", font=("Arial", 22)).pack(pady=20)
        
        # Simulação de cardápio
        cardapio = buscar_cardapio()

        for item in cardapio:
            frame_item = ctk.CTkFrame(self.main_frame)
            frame_item.pack(pady=10, fill="x", padx=40)

            nome = item["nome"]
            preco = f"R${item["preco"]:.2f}"
            categoria = item.get("categoria", "não informado")

            texto = f"{nome} | Preço: {preco} | Categoria: {categoria}"
            if "tamanho" in item:
                texto += f" | Tamanho: {item['tamanho']}"
            if "descricao" in item:
                texto += f" | Descrição: {item['descricao']}"

            label = ctk.CTkLabel(frame_item, text=texto, anchor="w")
            label.pack(side="left", padx=10, pady=5, fill="x", expand=True)

            def deletar(nome_item=nome):
                from db import deletar_item
                deletar_item(nome_item)
                self._atualizar_conteudo_cardapio()

            btn_del = ctk.CTkButton(frame_item, text="Excluir", width=80, command=deletar)
            btn_del.pack(side="right", padx=10)

            def editar(item=item):
                self._mostrar_edicao(item)

            btn_editar = ctk.CTkButton(frame_item, text="Editar", width=80, command=editar)
            btn_editar.pack(side="right", padx=10)

    def _mostrar_edicao(self, item):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        ctk.CTkLabel(self.main_frame, text=f"Editando: {item['nome']}", font=("Arial", 20)).pack(pady=20)

        nome_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Nome")
        nome_entry.insert(0, item['nome'])
        nome_entry.pack(pady=5)

        preco_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Preço")
        preco_entry.insert(0, str(item['preco']))
        preco_entry.pack(pady=5)

        categoria_menu = ctk.CTkOptionMenu(self.main_frame, values=['bebidas', 'prato', 'sobremesa'])
        categoria_menu.set(item['categoria'])
        categoria_menu.pack(pady=5)

        tamanho_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Tamanho")
        if item['tamanho']:
            tamanho_entry.insert(0, item['tamanho'])
        tamanho_entry.pack(pady=5)

        descricao_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Descrição")
        if item['descricao']:
            descricao_entry.insert(0, item['descricao'])
        descricao_entry.pack(pady=5)

        resultado_label = ctk.CTkLabel(self.main_frame, text="")
        resultado_label.pack(pady=5)

        def salvar_edicao():
            from db import editar_item
            try:
                preco = float(preco_entry.get())
            except ValueError:
                resultado_label.configure(text="Preço inválido!", text_color="red")
                return

            editar_item(
                item['id'],
                nome_entry.get(),
                preco,
                categoria_menu.get(),
                tamanho_entry.get(),
                descricao_entry.get()
            )
            resultado_label.configure(text="Item atualizado com sucesso!", text_color="green")
            self._atualizar_conteudo_cardapio()
        ctk.CTkButton(self.main_frame, text="Salvar", command=salvar_edicao).pack(pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()