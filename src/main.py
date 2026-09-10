from palavras import lista_palavras, sortear_palavras
from tabuleiro import estrutura_tabuleiro, gerar_categorias, exibir_tabuleiro
from tabuleiro import revelar_palavra
from jogo import trocar_turno, verificar_palpite

def main():
    print("=" * 40)
    print("          CODENAMES - PYTHON")
    print("=" * 40)

    print("\nBem-vindo ao Codenames!")

    input("\nPressione Enter para iniciar...")

    palavras_partida = sortear_palavras(lista_palavras, 25)
    categorias_geradas = gerar_categorias(False, True)

    tabuleiro = estrutura_tabuleiro(palavras_partida, categorias_geradas)

    equipe_atual = "vermelho"

    print(f"\nTurno da equipe: {equipe_atual.upper()}")

    print("\n--- VISÃO DOS JOGADORES ---")
    exibir_tabuleiro(tabuleiro, modo_mestre=False)

    print("\n--- VISÃO DO MESTRE ---")
    exibir_tabuleiro(tabuleiro, modo_mestre=True)

    jogo_ativo = True

    while jogo_ativo:
        print(f"\nTurno da equipe: {equipe_atual.upper()}")

        palpite = input("Digite a palavra que deseja palpitar: ")

        resultado = revelar_palavra(tabuleiro, palpite)
        resultado_palpite = verificar_palpite(resultado, equipe_atual)

        if resultado_palpite == "acerto":
            print(f"\nAcertou uma palavra da equipe {equipe_atual.upper()}!")
            print("A equipe pode continuar jogando.")

        elif resultado_palpite == "fim_turno":
            print("\nFim do turno.")

            equipe_atual = trocar_turno(equipe_atual)

            print(f"Agora é a vez da equipe {equipe_atual.upper()}.")

        elif resultado_palpite == "derrota":
            print(f"\nA equipe {equipe_atual.upper()} encontrou o ASSASSINO!")
            print("Fim de jogo.")

            jogo_ativo = False

        elif resultado_palpite == "invalido":
            print(f"\n{resultado}")

        exibir_tabuleiro(tabuleiro, modo_mestre=False)

main()
