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
