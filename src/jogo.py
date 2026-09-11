import os

def trocar_turno(equipe_atual: str) -> str:
    """Alterna a vez do jogo entre a equipe vermelha e a equipe azul.

    Args:
        equipe_atual: O nome da equipe que acabou de jogar ("vermelho" ou "azul").

    Returns:
        O nome da equipe adversária que jogará no próximo turno.

    Raises:
        ValueError: Se a equipe fornecida for diferente de "vermelho" ou "azul".
    """
    if equipe_atual == "vermelho":
        return "azul"

    if equipe_atual == "azul":
        return "vermelho"

    raise ValueError("Equipe inválida.")

def verificar_palpite(categoria: str, equipe_atual: str) -> str:
    """Avalia o resultado do palpite com base na categoria da palavra e na equipe atual.

    Args:
        categoria: A categoria da palavra revelada ("vermelho", "azul", "neutro", "assasino").
        equipe_atual: O nome da equipe que fez o palpite.

    Returns:
        O status do palpite ("acerto", "fim_turno", "derrota" ou "invalido").
    """
    if categoria == equipe_atual:
        return "acerto"

    if categoria == "neutro":
        return "fim_turno"

    if categoria == "assasino":
        return "derrota"

    if categoria in ["vermelho", "azul"]:
        return "fim_turno"

    return "invalido"

def verificar_vitoria(tabuleiro: list[list[dict]], equipe: str) -> bool:
    """Verifica se uma equipe já revelou todas as suas palavras no tabuleiro.

    Args:
        tabuleiro: Matriz 5x5 das cartas do jogo.
        equipe: Nome da equipe para verificação de vitória ("vermelho" ou "azul").

    Returns:
        True se a equipe tiver revelado todas as suas palavras, False caso contrário.
    """
    for linha in tabuleiro:
        for carta in linha:
            if carta["categoria"] == equipe and not carta["revelada"]:
                return False

    return True

def menu_inicial(opcoes_validas: list[str]) -> str:
    """Exibe o menu principal e solicita uma opção válida ao usuário.

    Args:
        opcoes_validas: Lista de strings contendo as opções aceitas pelo menu.

    Returns:
        A opção escolhida pelo usuário.
    """
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Iniciar partida")
        print("2 - Como jogar")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao in opcoes_validas:
            return opcao

        print("Opção inválida. Tente novamente.")

def limpar_tela(sistema_operacional: str) -> bool:
    """Limpa o console do terminal de acordo com o sistema operacional.

    Args:
        sistema_operacional: O nome do sistema operacional (ex: "nt" para Windows).

    Returns:
        True confirmando a execução da limpeza.
    """
    if sistema_operacional == "nt":
        os.system("cls")
    else:
        os.system("clear")

    return True