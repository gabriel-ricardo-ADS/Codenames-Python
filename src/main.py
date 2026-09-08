from palavras import lista_palavras, sortear_palavras
from tabuleiro import estrutura_tabuleiro, gerar_categorias, exibir_tabuleiro


def main():
    print("=" * 40)
    print("          CODENAMES - PYTHON")
    print("=" * 40)

    print("\nBem-vindo ao Codenames!")

    input("\nPressione Enter para iniciar...")

    palavras_partida = sortear_palavras(lista_palavras, 25)
    categorias_geradas = gerar_categorias(False, True)

    tabuleiro = estrutura_tabuleiro(palavras_partida, categorias_geradas)

    print("\n--- VISÃO DOS JOGADORES ---")
    exibir_tabuleiro(tabuleiro, modo_mestre=False)

    print("\n--- VISÃO DO MESTRE ---")
    exibir_tabuleiro(tabuleiro, modo_mestre=True)


if __name__ == "__main__":
    main()