from palavras import lista_palavras, sortear_palavras
from tabuleiro import estrutura_tabuleiro, gerar_categorias


def main():
    print("=" * 40)
    print("          CODENAMES - PYTHON")
    print("=" * 40)

    print("\nBem-vindo ao Codenames!")

    input("\nPressione Enter para iniciar...")

    palavras_partida = sortear_palavras(lista_palavras, 25)

    print("\nPalavras sorteadas:")
    print(palavras_partida)

    categorias_geradas = gerar_categorias(False, True)

    est_gerada = estrutura_tabuleiro(palavras_partida, categorias_geradas)
    print(est_gerada)

if __name__ == "__main__":
    main()