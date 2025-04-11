import customtkinter as ctk
from main import restaurante_praca 

ctk.set_appearance_mode('System') # 'Dark', "Light", "System";
ctk.set_default_color_theme('blue') # Pode usar: "blue", "green", "dark-blue";

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Sistema de Restaurante')
        self.geometry('600x400')

        self.label_titulo = ctk.CTkLabel(self, text=f'Cardápio do {restaurante_praca._nome}', font=('Arial', 20))
        self.label_titulo.pack(pady=20)

        self.texto_cardapio = ctk.CTkTextbox(self, width=500, height=200)
        self.texto_cardapio.pack()

        self.botao_lista = ctk.CTkButton(self, text='Exibir cardápio', command=self.exibir_cardapio)
        self.botao_lista.pack(pady=10)

    def exibir_cardapio(self):
        self.texto_cardapio.delete('0.0','end')
        for i, item in enumerate(restaurante_praca._cardapio, start=1):
            if hasattr(item, 'descricao'):
                linha = f"{i}. {item._nome} | R${item._preco: .2f} | {item.descricao}\n"
            else: 
                linha = f"{i}. {item._nome} | R${item._preco:.2f} | Tamanho: {item.tamanho}\n"
            self.texto_cardapio.insert("end", linha)
if __name__ == "__main__":
    app = App()
    app.mainloop()