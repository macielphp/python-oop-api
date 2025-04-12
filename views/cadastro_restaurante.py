import customtkinter as ctk
def mostrar_cadastro_restaurante(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        ctk.CTkLabel(self.main_frame, text="Cadastrar Novo Restaurante", font=("Arial", 20)).pack(pady=20)

        nome_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Nome do restaurante")
        nome_entry.pack(pady=5)

        avaliacao_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Avaliação (1 a 10)")
        avaliacao_entry.pack(pady=5)

        estado_menu = ctk.CTkOptionMenu(self.main_frame, values=["ativo", "inativo"])
        estado_menu.set("ativo")
        estado_menu.pack(pady=5)

        resultado_label = ctk.CTkLabel(self.main_frame, text="")
        resultado_label.pack(pady=5)

        def cadastrar_restaurante():
            from database.db import inserir_restaurante

            nome = nome_entry.get()
            avaliacao = avaliacao_entry.get()
            estado = estado_menu.get()

            if not nome or not avaliacao:
                resultado_label.configure(text="Nome e avaliação são obrigatórios!", text_color="red")
                return

            try:
                avaliacao = int(avaliacao)
                if not (1 <= avaliacao <= 10):
                    raise ValueError()
            except ValueError:
                resultado_label.configure(text="Avaliação dever ser um número entre 1 a 10.", text_color="red")
                return
            
            inserir_restaurante(nome, avaliacao, estado)
            resultado_label.configure(text="Restaurante cadastrado com sucesso!", text_color="green")

            nome_entry.delete(0, "end")
            avaliacao_entry.delete(0, "end")
            estado_menu.set("ativo")
        ctk.CTkButton(self.main_frame, text="Cadastrar", command=cadastrar_restaurante).pack(pady=10)