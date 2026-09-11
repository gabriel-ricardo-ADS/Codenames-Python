from random import shuffle

def gerar_categorias(jogador_azul: bool, jogador_vermelho: bool) -> list[str]:
    """Gera e embaralha a lista de categorias das cartas do tabuleiro.

    Args:
        jogador_azul: Booleano indicando se a equipe azul inicia a partida.
        jogador_vermelho: Booleano indicando se a equipe vermelha inicia a partida.

    Returns:
        Uma lista embaralhada contendo as 25 categorias da partida.
    """
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

def estrutura_tabuleiro(palavras: list[str], categorias: list[str]) -> list[list[dict]]:
    """Monta a matriz 5x5 do tabuleiro com palavras, categorias e estado de revelação.

    Args:
        palavras: Lista com as 25 palavras sorteadas.
        categorias: Lista com as 25 categorias correspondentes.

    Returns:
        Uma matriz 5x5 onde cada elemento é um dicionário representando uma carta.
    """
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

COR_RESET = "\033[0m"             # Reseta todas as cores e estilos

COR_VERMELHO = "\033[91;1m"       # Texto vermelho brilhante/negrito
COR_AZUL = "\033[94;1m"           # Texto azul brilhante/negrito
COR_NEUTRO = "\033[90m"           # Texto cinza escuro
COR_ASSASSINO = "\033[95;1m"      # Texto roxo/magenta brilhante

FUNDO_VERMELHO = "\033[41;97;1m"  # Fundo vermelho com texto branco/negrito
FUNDO_AZUL = "\033[44;97;1m"      # Fundo azul com texto branco/negrito
FUNDO_NEUTRO = "\033[100;97;1m"   # Fundo cinza com texto branco/negrito
FUNDO_ASSASSINO = "\033[45;97;1m" # Fundo roxo/magenta com texto branco/negrito

def obter_cor_categoria(categoria: str) -> str:
    """Retorna o código de cor ANSI correspondente à categoria da carta.

    Args:
        categoria: Nome da categoria ("vermelho", "azul", "neutro", "assasino").

    Returns:
        O código de escape ANSI relativo à cor da categoria.
    """
    if categoria == "vermelho":
        return COR_VERMELHO
    elif categoria == "azul":
        return COR_AZUL
    elif categoria == "neutro":
        return COR_NEUTRO
    elif categoria == "assasino":
        return COR_ASSASSINO
    return COR_RESET

def contar_cartas_restantes(tabuleiro: list[list[dict]]) -> tuple[int, int]:
    """Conta quantas cartas não reveladas restam para as equipes vermelha e azul.

    Args:
        tabuleiro: Matriz 5x5 das cartas do jogo.

    Returns:
        Uma tupla contendo a quantidade de cartas restantes (vermelho, azul).
    """
    restantes_vermelho = 0
    restantes_azul = 0
    for linha in tabuleiro:
        for carta in linha:
            if not carta["revelada"]:
                if carta["categoria"] == "vermelho":
                    restantes_vermelho += 1
                elif carta["categoria"] == "azul":
                    restantes_azul += 1
    return restantes_vermelho, restantes_azul

def exibir_tabuleiro(tabuleiro: list[list[dict]], modo_mestre: bool = False) -> None:
    """Exibe o tabuleiro formatado no terminal.

    Args:
        tabuleiro: Matriz 5x5 representando as cartas do jogo.
        modo_mestre: Se True, exibe o mapa secreto com todas as cores visíveis.
    """
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

            if carta["revelada"]:
                if carta["categoria"] == "vermelho":
                    texto_carta = f"{FUNDO_VERMELHO}{texto_alinhado}{COR_RESET}"

                elif carta["categoria"] == "azul":
                    texto_carta = f"{FUNDO_AZUL}{texto_alinhado}{COR_RESET}"

                elif carta["categoria"] == "neutro":
                    texto_carta = f"{FUNDO_NEUTRO}{texto_alinhado}{COR_RESET}"

                elif carta["categoria"] == "assasino":
                    texto_carta = f"{FUNDO_ASSASSINO}{texto_alinhado}{COR_RESET}"

                else:
                    texto_carta = texto_alinhado

            elif modo_mestre:
                cor = obter_cor_categoria(carta["categoria"])
                texto_carta = f"{cor}{texto_alinhado}{COR_RESET}"

            else:
                texto_carta = texto_alinhado

            linha_str += f"[ {texto_carta} ] "

        print(linha_str)

    print("=" * 95)

    restantes_vermelho, restantes_azul = contar_cartas_restantes(tabuleiro)
    print(f"Cartas Faltantes -> {COR_VERMELHO}Equipe Vermelha: {restantes_vermelho}{COR_RESET} | {COR_AZUL}Equipe Azul: {restantes_azul}{COR_RESET}")

    if modo_mestre:
        print(f"Legenda: {COR_VERMELHO}Vermelho{COR_RESET} | {COR_AZUL}Azul{COR_RESET} | {COR_NEUTRO}Neutro{COR_RESET} | {COR_ASSASSINO}Assassino{COR_RESET}")

    print("=" * 95)

def revelar_palavra(tabuleiro: list[list[dict]], palavra_buscada: str) -> str:
    """Procura uma palavra no tabuleiro e altera seu estado para revelada.

    Args:
        tabuleiro: Matriz 5x5 do tabuleiro de jogo.
        palavra_buscada: A palavra enviada pela equipe para palpite.

    Returns:
        A categoria da palavra revelada, ou uma mensagem de erro/aviso.
    """
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

