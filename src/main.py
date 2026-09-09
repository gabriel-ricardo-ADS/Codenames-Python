from palavras import lista_palavras, sortear_palavras
from tabuleiro import estrutura_tabuleiro, gerar_categorias, exibir_tabuleiro
from tabuleiro import revelar_palavra
from jogadores import cadastrar_jogadores, dividir_equipes, escolher_mestre, definir_equipe_inicial

VERDE = "\033[32m"
RESET = "\033[0m"

def main():
    print("=" * 40)
    print(f"          CODENAMES - {VERDE}PYTHON{RESET}")
    print("=" * 40)

    print(f"\nBem-vindo ao Codenames!")

    input("\nPressione Enter para iniciar...")

    #Cadastro dos jogadores
    jogadores = cadastrar_jogadores()

    #Divisao das equipes
    equipe_vermelha, equipe_azul = dividir_equipes(jogadores)

    #Escolha dos mestres-espioes
    mestre_vermelho = escolher_mestre(equipe_vermelha, "VERMELHA")
    mestre_azul = escolher_mestre(equipe_azul, "AZUL")

    #Quem inicia o jogo
    equipe_inicial = definir_equipe_inicial()

    palavras_partida = sortear_palavras(lista_palavras, 25)
    categorias_geradas = gerar_categorias(False, True)

    tabuleiro = estrutura_tabuleiro(palavras_partida, categorias_geradas)

    print("\n--- VISÃO DOS JOGADORES ---")
    exibir_tabuleiro(tabuleiro, modo_mestre=False)

    print("\n--- VISÃO DO MESTRE ---")
    exibir_tabuleiro(tabuleiro, modo_mestre=True)

    palpite = input("Digite a palavra que deseja palpitar: ")

    resultado = revelar_palavra(tabuleiro, palpite)

    print("Resultado:", resultado)
    exibir_tabuleiro(tabuleiro, modo_mestre=False)

main()
