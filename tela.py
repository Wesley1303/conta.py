import tkinter as tk


def login():
    # Coleta os dados digitados nos campos usando .get()
    email = input_email.get()
    senha = input_senha.get()

    # Validação básica de campos vazios
    if not email or not senha:
        label_status.config(
            text="Por favor, preencha todos os campos.", fg="#FF6B6B"
        )
        return

    # Exibe a informação capturada diretamente na interface do app
    texto_sucesso = f"Login enviado!\nEmail: {email}\nSenha: {senha}"
    label_status.config(text=texto_sucesso, fg="#1DD1A1")


# Configuração principal da Janela (Design Clean)
app = tk.Tk()
app.title("Sistema de Autenticação")
app.geometry("450x550")
app.configure(bg="#2F3640")  # Fundo escuro profissional

# Título da Tela
label_titulo = tk.Label(
    app,
    text="ÁREA DE ACESSO",
    font=("Helvetica", 16, "bold"),
    bg="#2F3640",
    fg="#F5F6FA",
)
label_titulo.pack(pady=(40, 30))

# --- CONTAINER DE E-MAIL ---
label_email = tk.Label(
    app,
    text="Endereço de E-mail:",
    font=("Helvetica", 11),
    bg="#2F3640",
    fg="#DCDDE1",
)
label_email.pack(anchor="w", padx=60, pady=(10, 2))

input_email = tk.Entry(
    app,
    font=("Helvetica", 12),
    bg="#3F4756",
    fg="#FFFFFF",
    bd=0,
    highlightthickness=1,
    highlightbackground="#718093",
    highlightcolor="#00A8FF",
)
# Define largura do campo e margens internas (padding artificial)
input_email.pack(fill="x", padx=60, ipady=6)

# --- CONTAINER DE SENHA ---
label_senha = tk.Label(
    app, text="Senha:", font=("Helvetica", 11), bg="#2F3640", fg="#DCDDE1"
)
label_senha.pack(anchor="w", padx=60, pady=(20, 2))

input_senha = tk.Entry(
    app,
    show="*",
    font=("Helvetica", 12),
    bg="#3F4756",
    fg="#FFFFFF",
    bd=0,
    highlightthickness=1,
    highlightbackground="#718093",
    highlightcolor="#00A8FF",
)
input_senha.pack(fill="x", padx=60, ipady=6)

# --- BOTÃO DE ENVIO ---
botao = tk.Button(
    app,
    text="ENTRAR NO SISTEMA",
    font=("Helvetica", 11, "bold"),
    bg="#00A8FF",
    fg="#FFFFFF",
    activebackground="#0097E6",
    activeforeground="#FFFFFF",
    bd=0,
    cursor="hand2",
)
botao.config(command=login)
botao.pack(fill="x", padx=60, pady=(40, 20), ipady=10)

# --- ÁREA DE FEEDBACK / RESULTADO (Substitui o Terminal) ---
label_status = tk.Label(
    app,
    text="",
    font=("Helvetica", 11, "italic"),
    bg="#2F3640",
    justify="left",
)
label_status.pack(pady=20, padx=60, fill="x")

app.mainloop()