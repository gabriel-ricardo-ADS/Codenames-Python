from random import shuffle

def estrutura_tabuleiro():
    matriz = []
    for l in range(5):
        linha = []
        for j in range(5):
            cat_vazia = " "
            linha.append(cat_vazia)
        matriz.append(linha)
    return matriz

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


