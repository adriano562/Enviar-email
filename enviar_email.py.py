import smtplib
from tkinter import *
from email.mime.text import MIMEText

janela = Tk()
janela.title("EMAIL BOT PRO")
janela.config(bg="#0b0f19")
janela.geometry("420x600")

frame = Frame(janela, bg="#0b0f19")
frame.pack(fill="both", expand=True, padx=20, pady=20)

def enviar_email():
    remetente = entry_remetente.get()
    senha = entry_senha.get()
    destinatario = entry_destinatario.get()
    assunto = entry_assunto.get()
    mensagem = text_mensagem.get("1.0", END)

    msg = MIMEText(mensagem)
    msg["Subject"] = assunto
    msg["From"] = remetente
    msg["To"] = destinatario

    try:
        status.config(text="Enviando...")
        janela.update()

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(remetente, senha)
        server.send_message(msg)
        server.quit()

        status.config(text="Email enviado com sucesso ✔")

    except Exception as e:
        status.config(text=f"Erro: {e}")

titulo = Label(frame, text="Mail Sender Pro", font=("Arial", 20, "bold"), bg="#0b0f19", fg="#a855f7")
titulo.pack(pady=15)

def criar_label(texto):
    return Label(frame, text=texto, bg="#0b0f19", fg="white")

def criar_entry(show=None):
    return Entry(frame, width=40, bg="#1f2937", fg="white", insertbackground="white", relief="flat", show=show)

criar_label("Seu e-mail").pack(anchor="w")
entry_remetente = criar_entry()
entry_remetente.pack(pady=5)

criar_label("Senha").pack(anchor="w")
entry_senha = criar_entry(show="*")
entry_senha.pack(pady=5)

criar_label("Destinatário").pack(anchor="w")
entry_destinatario = criar_entry()
entry_destinatario.pack(pady=5)

criar_label("Assunto").pack(anchor="w")
entry_assunto = criar_entry()
entry_assunto.pack(pady=5)

criar_label("Mensagem").pack(anchor="w")
text_mensagem = Text(frame, height=8, width=40, bg="#1f2937", fg="white", insertbackground="white", relief="flat")
text_mensagem.pack(pady=5)

Button(frame, text="ENVIAR EMAIL", bg="#a855f7", fg="white", activebackground="#7c3aed", activeforeground="white", padx=10, pady=8, bd=0, command=enviar_email).pack(pady=15)

status = Label(frame, text="", bg="#0b0f19", fg="#22c55e", font=("Arial", 10))
status.pack()
