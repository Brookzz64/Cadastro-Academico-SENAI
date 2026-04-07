import calculos
import utils
import arquivo
import analise_numpy as an

class Disciplina:
    

    def __init__(self, nome, av1, av2, av3, edag):
       """
       Inicializa a classe disciplina
       """
       self.nome = nome
       self.av1 = float(av1)
       self.av2 = float(av2)
       self.av3 = float(av3)
       self.edag = float(edag)
       self.media = calculos.calcular_media(self.av1, self.av2, self.av3, self.edag)
       self.situacao = calculos.verificar_status_aprovacao(self.media)
       self.final = None

    
class HistoricoAcademico:
   def cadastrar(self):
       """ 
       Estrutura de repetição capaz de registar nome de uma disciplina, assim como as suas notas da AV1,AV2
       AV3 e EDAG. Alem disso utiliza duas outras funções para armazenar tudo na mesma biblioteca, ficando 
       ficando pronto para a impressão no fim do código.
       """
    
       while True:
           nome = utils.ler_str("\n\nDigite o nome da disciplina, ou (sair) para encerrar:\n").strip().upper()
           if nome.lower() == "sair":
              break
           
           for disciplina_salva in arquivo.ler_todas_disciplinas():
               if disciplina_salva.nome == nome:
                   print("Essa disciplina ja foi registrada. \n")
                   Menu(self)
                   break

           A1 = utils.ler_float("Nota AV1: ")
           A2 = utils.ler_float("Nota AV2: ")
           A3 = utils.ler_float("Nota AV3: ")
           EDAG = utils.ler_float("Nota EDAG: ")
        
           disciplina = Disciplina(nome, A1, A2, A3, EDAG)

           arquivo.salvar_disciplina(disciplina)
       Menu(self)

   def imprimir_disciplina(self):
       while True:
           if not arquivo.ler_todas_disciplinas():
               print("Nenhuma disciplina registrada! \n")
               Menu(self)

           nome = utils.ler_str("Digite o nome da disciplina: \n").strip().upper()

           b = arquivo.ler_disciplina(nome)

           while True:
                if b.nome.upper() == nome.strip().upper():
                    print(f"\n\n\n--{b.nome}--\n  notas  \nAV1: {b.av1:.2f} "
                    f"\nAV2: {b.av2:.2f} \nAV3: {b.av3:.2f} "
                    f"\nEDAG: {b.edag:.2f} \n---------------"
                    f"\nMédia: {b.media:.2f} "
                    f"\nSituação: {b.situacao}")

                    if b.final != None:
                        print(f"\nProva Final: {b.final:.2f}")
                    
                    print("\n\n")

                    Menu(self)
                    break
                else:
                    print("Nenhuma disciplina encontrada! \n")
               

   def imprimir_disciplinas_recursivo(self, indice = 0):
       """
       função recursiva para imprimir as disciplinas com suas respectivas notas, medias e situações
       """

       lista = arquivo.ler_todas_disciplinas()

       if indice >= len(lista):
           Menu(self)
           return
    
       b = lista[indice]
    
       print(f"\n\n\n--{b.nome}--\n  notas  \nAV1: {b.av1:.2f} "
                    f"\nAV2: {b.av2:.2f} \nAV3: {b.av3:.2f} "
                    f"\nEDAG: {b.edag:.2f} \n---------------"
                    f"\nMédia: {b.media:.2f} "
                    f"\nSituação: {b.situacao}")

       if b.final != None:
           print(f"\nProva Final: {b.final:.2f}")
                    
       print("\n\n")
       
       self.imprimir_disciplinas_recursivo(indice + 1)

   def alterar_nota(self):
       while True:
           if not arquivo.ler_todas_disciplinas():
               print("Nenhuma disciplina registrada! \n")
               Menu(self)
               
           nome = utils.ler_str("Digite o nome da disciplina: \n")

           for b in arquivo.ler_todas_disciplinas():
                if b.nome.upper() == nome.upper():
                    print(f"av 1: {b.av1:.2f} \n")
                    print(f"av 2: {b.av2:.2f} \n")
                    print(f"av 3: {b.av3:.2f} \n")
                    print(f"EDAG: {b.edag:.2f} \n")

                    while True:
                        av = utils.ler_str("Qual a avaliação a mudar?\n").lower().strip()
                        if av == "av1" or av == "av2" or av == "av3" or av == "edag":
                            break
                        else:
                            print("Avaliação inválida. \n")

                    nota = utils.ler_float("Digite a nota nova: \n")
                        
                    if av == "av1":
                        b.av1 = nota
                    elif av == "av2":
                        b.av2 = nota
                    elif av == "av3":
                        b.av3 = nota
                    elif av == "edag":
                        b.edag = nota

                    b.media = calculos.calcular_media(b.av1, b.av2, b.av3, b.edag)

                    arquivo.remover_disciplina(b.nome.upper())
                    arquivo.salvar_disciplina(b)

                    Menu(self) 

                    return
                else:
                    print("Nenhuma disciplina encontrada! \n")

   def excluir_disciplina(self):
       while True:
           if not arquivo.ler_todas_disciplinas():
               print("Nenhuma disciplina registrada! \n")
               Menu(self)
           nome = utils.ler_str("Digite o nome da disciplina a ser removida: \n")

           for b in arquivo.ler_todas_disciplinas():
                if b.nome.upper() == nome.upper():
                    
                    print(f"Disciplina {b.nome} removida. \n")
                    arquivo.remover_disciplina(b.nome.upper())

                    Menu(self) 

                    return
                else:
                    print("Nenhuma disciplina encontrada! \n")

   def lancar_nota_final(self):
       while True:
           if not arquivo.ler_todas_disciplinas():
               print("Nenhuma disciplina registrada! \n")
               Menu(self)

           nome = utils.ler_str("Digite o nome da disciplina: \n")

           for b in arquivo.ler_todas_disciplinas():
                if b.nome.upper() == nome.upper():
                    final = utils.ler_float("Digite a nota da prova final: \n")

                    b.final = final

                    b.situacao = calculos.verificar_aprovação_final(final)

                    arquivo.remover_disciplina(b.nome.upper())
                    arquivo.salvar_disciplina(b)

                    Menu(self)
                    break
                else:
                    print("Nenhuma disciplina encontrada! \n")
