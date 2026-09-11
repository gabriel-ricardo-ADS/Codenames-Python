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

COR_RESET = "\033[0m"
COR_VERMELHO = "\033[91;1m"     # Vermelho brilhante/negrito
COR_AZUL = "\033[94;1m"         # Azul brilhante/negrito
COR_NEUTRO = "\033[90m"         # Cinza escuro (Neutro)
COR_ASSASSINO = "\033[95;1m" # Texto roxo/magenta (sem fundo)

def obter_cor_categoria(categoria):
    if categoria == "vermelho":
        return COR_VERMELHO
    elif categoria == "azul":
        return COR_AZUL
    elif categoria == "neutro":
        return COR_NEUTRO
    elif categoria == "assasino":
        return COR_ASSASSINO
    return COR_RESET

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
            texto_alinhado = carta["palavra"].center(13)
            if modo_mestre:
                cor = obter_cor_categoria(carta["categoria"])
                if carta["revelada"]:
                    texto_carta = f"\033[47m{cor}{texto_alinhado}{COR_RESET}"
                else:
                    texto_carta = f"{cor}{texto_alinhado}{COR_RESET}"
            elif carta["revelada"]:
                cor = obter_cor_categoria(carta["categoria"])
                texto_carta = f"{cor}{texto_alinhado}{COR_RESET}"
            else:
                texto_carta = texto_alinhado
            linha_str += f"[ {texto_carta} ] "
        print(linha_str)

    print("=" * 95)
    if modo_mestre:
        print(f"Legenda: {COR_VERMELHO}Vermelho{COR_RESET} | {COR_AZUL}Azul{COR_RESET} | {COR_NEUTRO}Neutro{COR_RESET} | {COR_ASSASSINO}Assassino{COR_RESET} | \033[47;30mFundo Branco\033[0m = Revelada")
        print("=" * 95)

def revelar_palavra(tabuleiro, palavra_buscada):
    palavra_buscada = palavra_buscada.strip().upper()
    for linha in tabuleiro:
        for carta in linha:
            if carta["palavra"].upper() == palavra_buscada:
                if not carta["revelada"]:
                    carta["revelada"] = True
                    return carta["categoria"]
                else:
                    return f"A palavra '{palavra_buscada}' ja foi revelada"
    return f"A palavra '{palavra_buscada}' nao foi encontrada"

