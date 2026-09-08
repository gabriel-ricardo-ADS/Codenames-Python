from palavras import lista_palavras, sortear_palavras


def main():
    print("=" * 40)
    print("          CODENAMES - PYTHON")
    print("=" * 40)

    print("\nBem-vindo ao Codenames!")

    input("\nPressione Enter para iniciar...")

    palavras_partida = sortear_palavras(lista_palavras, 25)

    print("\nPalavras sorteadas:")
    print(palavras_partida)


if __name__ == "__main__":
    main()