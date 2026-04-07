import tkinter as tk
from tkinter import messagebox
import usuarios
import main

def acao_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    if checar_campos():
        return
    if usuarios.checar_usuario(usuario, senha):
        janela.destroy()
        main.iniciar()
    else:
        pop_up("Aviso", "Usuario ou senha incorretos")

def acao_register():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    if checar_campos():
        return
    if usuarios.criar_usuario(usuario, senha):
        pop_up("Aviso", "Usuario registrado com sucesso!")
    else:
        pop_up("Aviso", "Usuario não disponivel")
    
def checar_campos():
    usuario = campo_usuario.get().strip()
    senha = campo_senha.get().strip()
    if usuario == "":
        pop_up("Aviso", "Usuario vazio")
        return True
    if senha == "":
        pop_up("Aviso", "Senha vazio")
        return True
    return False


def pop_up(nome, mensagem):
    messagebox.showwarning(nome, mensagem)

janela = tk.Tk()
janela.title("Monitoramentocad.exe")
janela.geometry("600x400")

janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=1)
janela.columnconfigure(2, weight=1)
janela.columnconfigure(3, weight=1)

titulo = tk.Label(janela, text="==Monitoramento Acadêmico==", font=("Arial, 22"))
titulo.grid(row=0, columnspan=2, padx=40, pady=40)

tk.Label(janela, text="Usuário:").grid(row=1, column=0, padx=40, pady=40, sticky="ew")
campo_usuario = tk.Entry(janela)
campo_usuario.grid(row=1, column=1, padx=40, pady=40, sticky="ew")

tk.Label(janela, text="Senha:").grid(row=2, column=0, padx=40, pady=40, sticky="ew")
campo_senha = tk.Entry(janela)
campo_senha.grid(row=2, column=1, padx=40, pady=40, sticky="ew")

botao_login = tk.Button(janela, text="Login", command=acao_login)
botao_login.grid(row=3, column=0, columnspan=2, pady=10)

botao_register = tk.Button(janela, text="Registrar", command=acao_register)
botao_register.grid(row=3, column=1, columnspan=2, pady=10)

janela.mainloop()
