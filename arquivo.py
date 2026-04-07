import csv
import model

def salvar_disciplina(disciplina):
    with open("dados.csv", "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        final = disciplina.final
        if final == None:
            final = -1
        escritor.writerow([disciplina.nome, disciplina.av1, disciplina.av2, disciplina.av3, disciplina.edag, disciplina.media, disciplina.situacao, final])

def ler_disciplina(nome_disciplina):
    try:
        with open("dados.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                if linha[0] == nome_disciplina:
                    disciplina = model.Disciplina(linha[0], linha[1], linha [2], linha[3], linha[4])
                    disciplina.media = float(linha[5])
                    disciplina.situacao = linha[6]
                    final = float(linha[7])
                    if linha[7] == -1:
                        final = None
                    disciplina.final = final
                    return disciplina
            return None
    except:
        with open("dados.csv", "a", newline="", encoding="utf-8") as arquivo:
                ler_disciplina(nome_disciplina)
    
def ler_todas_disciplinas():
    try:
        disciplinas = []
        with open("dados.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                disciplina = model.Disciplina(linha[0], linha[1], linha [2], linha[3], linha[4])
                disciplina.media = float(linha[5])
                disciplina.situacao = linha[6]
                final = float(linha[7])
                if linha[7] == -1:
                    final = None
                disciplina.final = final
                disciplinas.append(disciplina)
        return disciplinas
    except:
        with open("dados.csv", "a", newline="", encoding="utf-8") as arquivo:
                ler_todas_disciplinas()


def remover_disciplina(nome_disciplina):
    try:
        linhas = []
        with open("dados.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            linhas = list(leitor)

        novas_linhas = [l for l in linhas if l[0].upper() != nome_disciplina.upper()]

        with open("dados.csv", "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerows(novas_linhas)
    except:
        with open("dados.csv", "a", newline="", encoding="utf-8") as arquivo:
                remover_disciplina(nome_disciplina)

    novas_linhas = [l for l in linhas if l[0].upper() != nome_disciplina.upper()]

    with open("dados.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(novas_linhas)
