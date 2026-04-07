import numpy as np
import model

def gerar_array_medias(materias):
    medias = []
    for materia in materias:
        medias.append(materia.media)
    
    return np.array(medias, np.float32)

def gerar_array_nomes(materias):
    nomes = []
    for materia in materias:
        nomes.append(materia.nome)
    
    return np.array(nomes, np.object_)

def exibir_array_medias(materias, hs):
    if not materias:
        print("Nenhuma disciplina registrada! \n")
        model.Menu(hs)
    
    medias = gerar_array_medias(materias)

    print(f"Medias: {medias} \nDType: {medias.dtype} \nFormato: {medias.shape}")
    model.Menu(hs)

def gerar_ranking_medias(materias, hs):
    if not materias:
        print("Nenhuma disciplina registrada! \n")
        model.Menu(hs)
    nomes = gerar_array_nomes(materias)
    medias = gerar_array_medias(materias)

    indexes = np.argsort(medias)[::-1]

    for i in range(indexes.size):
        print(f"{nomes[indexes[i]]}: Media {medias[indexes[i]]:.2f}")

    model.Menu(hs)

def estatisticas_gerais(materias):
    if not materias:
        return 0, 0, 0, 0 

    medias_numeros = gerar_array_medias(materias)
    
    media_geral = np.mean(medias_numeros)
    max_nota = np.max(medias_numeros)
    min_nota = np.min(medias_numeros)
    desvio = np.std(medias_numeros)

    return media_geral, max_nota, min_nota, desvio

def exibir_estatisticas_gerais(materias, hs):
    if not materias:
        print("Nenhuma disciplina para calcular estatísticas. \n")
        model.Menu(hs)
        return

    med, nota_max, nota_min, desv = estatisticas_gerais(materias)

    print("ESTATÍSTICAS GERAIS: ")
    print(f"Média geral: {med:.2f}")
    print(f"Maior média: {nota_max:.2f}")
    print(f"Menor média: {nota_min:.2f}")
    print(f"Desvio padrão: {desv:.2f}")

    model.Menu(hs)
