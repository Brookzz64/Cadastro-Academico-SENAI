
def calcular_media(av1, av2, av3, edag):
        """
        Função feita para calcular a média parcial das notas de uma disciplina e retornar a variavel media. Ela 
        recebe a nota de todas as avaliações da disciplina, e põe em uma formula que calcula sua média ponderada.
        """

        media = (av1 * 2.5 +av2 * 2.5 + av3 *3.0 + edag * 2) / 10
        return round(media, 2)

def verificar_status_aprovacao(media):
        """
        função feita para verificar os status de aprovação do usuario, julgando se está aprovado, re
        provado, ou em prova final. Recebe a variavel (media) e retorna a variavel (situacao).
        """
        
        if media >= 7:
            situacao = "aprovado"
        elif media >= 4:
            situacao = "prova final"
        else:
            situacao = "reprovado"
        return situacao

def verificar_aprovação_final(final):
        """
        função feita para verificar os status de aprovação na prova final usuario, julgando se está aprovado 
        ou reprovado, caso vá para prova final. Recebe a variavel (final) e retorna a variavel (situacao).
        """
        
        if final >= 5:
            situacao = "aprovado na final"
        else:
            situacao = "reprovado"
        return situacao

        """
        
        if final >= 5:
            situacao = "aprovado na final"
        else:
            situacao = "reprovado"
        return situação
