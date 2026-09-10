def trocar_turno(equipe_atual):
    if equipe_atual == "vermelho":
        return "azul"

    if equipe_atual == "azul":
        return "vermelho"

    raise ValueError("Equipe inválida.")

def verificar_palpite(categoria, equipe_atual):
    if categoria == equipe_atual:
        return "acerto"

    if categoria == "neutro":
        return "fim_turno"

    if categoria == "assasino":
        return "derrota"

    if categoria in ["vermelho", "azul"]:
        return "fim_turno"

    return "invalido"

def verificar_vitoria(tabuleiro, equipe):
    for linha in tabuleiro:
        for carta in linha:
            if carta["categoria"] == equipe and not carta["revelada"]:
                return False

    return True

def menu_inicial(opcoes_validas):
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Iniciar partida")
        print("2 - Como jogar")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao in opcoes_validas:
            return opcao

        print("Opção inválida. Tente novamente.")