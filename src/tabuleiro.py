from random import shuffle

def gerar_categorias(jogador_azul,jogador_vermelho):
    lista_cat = ["assasino"]
    if jogador_azul:
        for c in range(9):
            lista_cat.append("azul")
        for c in range(8):
            lista_cat.append("vermelho")
    elif jogador_vermelho:
        for c in range(9):
            lista_cat.append("vermelho")
        for c in range(8):
            lista_cat.append("azul")
    for n in range(7):
        lista_cat.append("neutro")

    shuffle(lista_cat)

    return lista_cat

def estrutura_tabuleiro(palavras, categorias):
    matriz = []
    indice = 0
    for l in range(5):
        linha = []
        for j in range(5):
            carta = {
                "palavra": palavras[indice],
                "categoria": categorias[indice],
                "revelada": False
            }
            linha.append(carta)
            indice += 1
        matriz.append(linha)
    return matriz

def exibir_tabuleiro(tabuleiro, modo_mestre=False):
    print("=" * 95)
    if modo_mestre:
        print(" " * 35 + "MAPA SECRETO DO MESTRE")
    else:
        print(" " * 38 + "TABULEIRO DO JOGO")
    print("=" * 95)

    for linha in tabuleiro:
        linha_str = ""
        for carta in linha:
            if modo_mestre:
                if carta["categoria"] == "assasino":
                    cat_tag = "X"
                elif carta["categoria"] == "vermelho":
                    cat_tag = "V"
                elif carta["categoria"] == "azul":
                    cat_tag = "A"
                else:
                    cat_tag = "N"
                texto_carta = f"{carta['palavra']} ({cat_tag})"
            else:
                if carta["revelada"]:
                    texto_carta = f"[{carta['categoria'].upper()}]"
                else:
                    texto_carta = carta["palavra"]

            linha_str += f"[ {texto_carta.ljust(13)} ] "
        print(linha_str)

    print("=" * 95)
    if modo_mestre:
        print("Legenda: (V) Vermelho | (A) Azul | (N) Neutro | (X) Assassino")
        print("=" * 95)
