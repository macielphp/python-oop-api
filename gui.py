import customtkinter as ctk
from main import restaurante_praca 

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
        self._atualizar_conteudo("Formulário de cadastro de item")

    def mostrar_avaliacoes(self):
        self._atualizar_conteudo("Página de avaliações")

    def _atualizar_conteudo(self, texto):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        ctk.CTkLabel(self.main_frame, text=texto, font=("Arial", 20)).pack(pady=50)

    def _atualizar_conteudo_cardapio(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        ctk.CTkLabel(self.main_frame, text="Cardápio do Restaurante Praça", font=("Arial", 22)).pack(pady=20)
        
        # Simulação de cardápio
        cardapio = [
            {"nome": "Suco de Melancia", "preco": 4.75, "tamanho": "grande"},
            {"nome": "Pãozinho", "preco": 1.84, "descricao": "O melhor pão da cidade"},
            {"nome": "Pet Gatou", "preco": 25.415, "descricao": "Chocolate belga Amarelo"}
        ]

        for item in cardapio:
            frame_item = ctk.CTkFrame(self.main_frame)
            frame_item.pack(pady=10, fill="x", padx=40)

            nome = item["nome"]
            preco = f"R${item["preco"]:.2f}"

            texto = f"{nome} | Preço: {preco}"
            if "tamanho" in item:
                texto += f" | Tamanho: {item['tamanho']}"
            if "descricao" in item:
                texto += f" | Descrição: {item['descricao']}"
            
            ctk.CTkLabel(frame_item, text=texto, anchor="w").pack(padx="10", pady="5")

if __name__ == "__main__":
    app = App()
    app.mainloop()