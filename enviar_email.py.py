import smtplib
from tkinter import *
from email.mime.text import MIMEText

janela = Tk()
janela.title("EMAIL BOT")
janela.config(bg="#121212")

frame = Frame(janela, bg="#121212")
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
        status["text"] = "Enviando..."
        janela.update()

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(remetente, senha)

        server.send_message(msg)
        server.quit()

        status["text"] = "Email enviado com sucesso!"

    except Exception as e:
        status["text"] = f"Erro: {e}"

titulo = Label(frame, text="Mail.py", font=("Arial", 20, "bold"),
               bg="#121212", fg="#00aaff")
titulo.pack(pady=10)


Label(frame, text="Seu e-mail", bg="#121212", fg="white").pack(anchor="w")
entry_remetente = Entry(frame, width=40)
entry_remetente.pack(pady=5)

Label(frame, text="Senha", bg="#121212", fg="white").pack(anchor="w")
entry_senha = Entry(frame, show="*", width=40)
entry_senha.pack(pady=5)

Label(frame, text="Destinatário", bg="#121212", fg="white").pack(anchor="w")
entry_destinatario = Entry(frame, width=40)
entry_destinatario.pack(pady=5)

Label(frame, text="Assunto", bg="#121212", fg="white").pack(anchor="w")
entry_assunto = Entry(frame, width=40)
entry_assunto.pack(pady=5)


Button(frame, text="ENVIAR >", bg="#1f6feb", fg="white",
       activebackground="#388bfd", padx=10, pady=5,
       command=enviar_email).pack(pady=10)

Label(frame, text="Mensagem:", bg="#121212", fg="white").pack(anchor="w")
text_mensagem = Text(frame, height=8, width=40, bg="#1e1e1e", fg="white")
text_mensagem.pack()

status = Label(frame, text="", bg="#121212", fg="#00ff88")
status.pack(pady=5)

janela.mainloop()