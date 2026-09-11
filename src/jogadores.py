import random

VERMELHO = "\033[31m"
AZUL = "\033[94;1m"
VERDE = "\033[32m"
RESET = "\033[0m"


def cadastrar_jogadores() -> list[dict]:
    """Solicita a quantidade e os nomes dos jogadores para cadastro.

    Returns:
        Uma lista de dicionários contendo os dados de cada jogador cadastrado.
    """
    jogadores = []

    print('=-' * 20)
    print(f'\nHora de Cadastrar os Jogadores!\n')
    print('=-' * 20)

    while True:
        try:
            num_jogadores = int(input('\nQuantos jogadores participarão? '))
            print()

            if num_jogadores < 4:
                raise ValueError('Número de jogadores não pode ser inferior a 4')

            if num_jogadores > 10:
                raise ValueError('Número de jogadores não pode ser superior a 10')

        except ValueError as erro:
            print(f'\n{VERMELHO}[ERRO]: {erro}{RESET}')
            continue

        else:
            print('=-' * 20)
            print(f'\n{VERDE}[SUCESSO]: Registrado {num_jogadores} jogadores{RESET}\n')
            print('=-' * 20)
            break

    for i in range(num_jogadores):
        while True:
            try:
                nome = input(f'\nDigite o nome do jogador {i + 1}: ').strip().title()

                if nome == '':
                    raise ValueError('O nome não pode ficar vazio')

                for jogador in jogadores:
                    if jogador['nome'].lower() == nome.lower():
                        raise ValueError("Esse nome já foi cadastrado.")

            except ValueError as erro:
                print(f'{VERMELHO}[ERRO]: {erro}{RESET}')
                continue

            else:
                break

        jogador = {
            "nome": nome,
            "equipe": None,
            "mestre_espiao": False
        }

        jogadores.append(jogador)

    print()
    print('=-' * 20)
    print(f'\n{VERDE}[SUCESSO]: Jogadores adicionados{RESET}\n')
    print('=-' * 20)

    return jogadores


def dividir_equipes(jogadores: list[dict]) -> tuple[list[dict], list[dict]]:
    """Divide a lista de jogadores entre a equipe vermelha e a equipe azul.

    Args:
        jogadores: Uma lista com todos os jogadores cadastrados.

    Returns:
        Uma tupla contendo duas listas de dicionários: (equipe_vermelha, equipe_azul).
    """
    equipe_vermelha = []
    equipe_azul = []

    for i in range(len(jogadores)):
        if i % 2 == 0:
            jogadores[i]["equipe"] = "VERMELHA"
            equipe_vermelha.append(jogadores[i])
        else:
            jogadores[i]["equipe"] = "AZUL"
            equipe_azul.append(jogadores[i])

    print(f'{VERMELHO}EQUIPE VERMELHA:{RESET}')
    for jogador in equipe_vermelha:
        print(jogador["nome"])
    print('=-' * 20)

    print(f'{AZUL}EQUIPE AZUL:{RESET}')
    for jogador in equipe_azul:
        print(jogador["nome"])
    print('=-' * 20)

    return equipe_vermelha, equipe_azul


def definir_cor(nome_equipe: str) -> str:
    """Retorna a constante de cor ANSI correspondente ao nome da equipe.

    Args:
        nome_equipe: Nome da equipe ("VERMELHA" ou "AZUL").

    Returns:
        O código ANSI correspondente à cor da equipe.
    """
    if nome_equipe == "VERMELHA":
        return VERMELHO
    elif nome_equipe == "AZUL":
        return AZUL
    else:
        return RESET


def escolher_mestre(equipe: list[dict], nome_equipe: str) -> dict:
    """Solicita a escolha do mestre-espião dentro de uma equipe.

    Args:
        equipe: Lista de jogadores pertencentes à equipe.
        nome_equipe: Nome da equipe selecionada ("VERMELHA" ou "AZUL").

    Returns:
        O dicionário do jogador definido como mestre-espião.
    """
    cor_equipe = definir_cor(nome_equipe)
    while True:
        try:
            print(f'\nEscolha o mestre-espião da equipe {cor_equipe}{nome_equipe}{RESET}:')

            for jogador in equipe:
                print(jogador["nome"])

            nome_mestre = input('\nDigite o nome do mestre-espião: ').strip().title()

            if nome_mestre == '':
                raise ValueError('O nome não pode ficar vazio')

            mestre_encontrado = None

            for jogador in equipe:
                if jogador["nome"].lower() == nome_mestre.lower():
                    mestre_encontrado = jogador
                    break

            if mestre_encontrado is None:
                raise ValueError('Esse jogador não existe/pertence a essa equipe')

        except ValueError as erro:
            print('=-' * 20)
            print(f'\n{VERMELHO}[ERRO]: {erro}{RESET}\n')
            print('=-' * 20)
            continue

        else:
            mestre_encontrado["mestre_espiao"] = True

            print('=-' * 20)
            print(f'\n{VERDE}[SUCESSO]: {mestre_encontrado["nome"]} é o mestre-espião da equipe {nome_equipe}{RESET}\n')
            print('=-' * 20)

            return mestre_encontrado


def definir_equipe_inicial() -> str:
    """Sorteia aleatoriamente qual equipe iniciará a partida.

    Returns:
        O nome da equipe sorteada ("VERMELHA" ou "AZUL").
    """
    equipe_inicial = random.choice(["VERMELHA", "AZUL"])
    cor_equipe = definir_cor(equipe_inicial)

    print(f'\nA equipe que começa é: {cor_equipe}{equipe_inicial}{RESET}\n')
    print('=-' * 20)

    return equipe_inicial