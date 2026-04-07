
import csv

def usuario_disponivel(usuario):
    try:
        with open("usuarios.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                if linha[0] == usuario:
                    return False
            return True
    except:
        with open("usuarios.csv", "a", newline="", encoding="utf-8") as arquivo:
                return usuario_disponivel(usuario)

def criar_usuario(usuario, senha):
    if not usuario_disponivel(usuario):
         return False
    with open("usuarios.csv", "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([usuario, senha])
        return True

def checar_usuario(usuario, senha):
    try:
        with open("usuarios.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                if linha[0] == usuario and linha[1] == senha:
                    return True
            return False
    except:
        with open("usuarios.csv", "a", newline="", encoding="utf-8") as arquivo:
                checar_usuario(usuario, senha)
