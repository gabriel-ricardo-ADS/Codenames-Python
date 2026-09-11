import random

#[cores]
VERMELHO = "\033[31m"
AZUL = "\033[94;1m"
VERDE = "\033[32m"
RESET = "\033[0m"

#[CADASTRO]
#[CADASTRO]
def cadastrar_jogadores() -> list[dict]:
    """Solicita a quantidade e os nomes dos jogadores para cadastro.

    Returns:
        Uma lista de dicionários contendo os dados de cada jogador cadastrado.

    Raises:
        ValueError: Se o número de jogadores for inferior a 4 ou superior a 10,
            ou se um nome fornecido for vazio ou duplicado.
    """
    #Listinha para guardar informações dos players
    jogadores = []

    print('=-' * 20)
    print(f'\nHora de Cadastrar os Jogadores!\n')
    print('=-' * 20)

    while True:

        try:
            #Recebimento da qtd de jogadores
            num_jogadores = int(input('\nQuantos jogadores participarão? '))
            print()

            #Validação: O funcionamento do jogo baseia-se no tabuleiro com no mínimo 4 jogadores ativos
            if num_jogadores < 4:
                raise ValueError('Número de jogadores não pode ser inferior a 4')

            if num_jogadores > 10:
                raise ValueError('Número de jogadores não pode ser superior a 10')
            
        except ValueError as erro:
            print(f'\n{VERMELHO}[ERRO]: {erro}{RESET}')
            continue

        #Confirmação, sai do while
        else:
            print('=-' * 20)
            print(f'\n{VERDE}[SUCESSO]: Registrado {num_jogadores} jogadores{RESET}\n')
            print('=-' * 20)
            break

    for i in range(num_jogadores):

        while True:

            try:
                #Recebimento de dados de cada jogador (strip para remoção de espaços)
                nome = input(f'\nDigite o nome do jogador {i + 1}: ').strip()

                #Validação: Nome não pode ser vazio
                if nome == '':
                    raise ValueError('O nome não pode ficar vazio')

                #Validação: Nome não pode ser igual ao de outro jogador
                for jogador in jogadores:
                    if jogador['nome'].lower() == nome.lower():
                        raise ValueError("Esse nome já foi cadastrado.")

            except ValueError as erro:
                print(f'{VERMELHO}[ERRO]: {erro}{RESET}')
                continue

            else:
                break

        #Dicionario para guardar multiplas info por jogador.
        jogador = {
            "nome": nome,
            "equipe": None,
            "mestre_espiao": False
        } #Por enquanto equipe e mestre não definidos.

        jogadores.append(jogador)

    #Retorna lista de jogadores cadastrados
    print()
    print('=-' * 20)
    print(f'\n{VERDE}[SUCESSO]: Jogadores adicionados{RESET}\n')
    print('=-' * 20)

    return jogadores

#[DIVISAO DE EQUIPES]
def dividir_equipes(jogadores: list[dict]) -> tuple[list[dict], list[dict]]:
    """Divide a lista de jogadores entre a equipe vermelha e a equipe azul.

    Args:
        jogadores: Uma lista com todos os jogadores cadastrados.

    Returns:
        Uma tupla contendo duas listas de dicionários: (equipe_vermelha, equipe_azul).
    """
    #Equipes!
    equipe_vermelha = []
    equipe_azul = []

    #Percorre todos os jogadores cadastrados
    for i in range(len(jogadores)):
        #Jogadores em posições pares vão para a equipe vermelha
        if i % 2 == 0:
            jogadores[i]["equipe"] = "VERMELHA"
            equipe_vermelha.append(jogadores[i])

        #Caso esteja em ímpar, vai para a azul
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
    
    #Retorna as duas equipes já separadas
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

    Raises:
        ValueError: Se o nome do mestre for vazio ou se o jogador não pertencer à equipe.
    """
    cor_equipe = definir_cor(nome_equipe)
    while True:
        try:
            print(f'\nEscolha o mestre-espião da equipe {cor_equipe}{nome_equipe}{RESET}:')

            #Mostra somente os nomes dos jogadores da equipe selecionada
            for jogador in equipe:
                print(jogador["nome"])

            nome_mestre = input('\nDigite o nome do mestre-espião: ').strip()

            #Validação: Nome não pode ser vazio
            if nome_mestre == '':
                raise ValueError('O nome não pode ficar vazio')

            #Procura o jogador dentro da equipe
            mestre_encontrado = None

            for jogador in equipe:
                if jogador["nome"].lower() == nome_mestre.lower():
                    mestre_encontrado = jogador
                    break

            #Validação: Jogador precisa pertencer à equipe
            if mestre_encontrado is None:
                raise ValueError('Esse jogador não existe/pertence a essa equipe')

        except ValueError as erro:
            print('=-' * 20)
            print(f'\n{VERMELHO}[ERRO]: {erro}{RESET}\n')
            print('=-' * 20)
            continue

        else:
            #Define o jogador como mestre-espião
            mestre_encontrado["mestre_espiao"] = True

            print('=-' * 20)
            print(f'\n{VERDE}[SUCESSO]: {mestre_encontrado["nome"]} é o mestre-espião da equipe {nome_equipe}{RESET}\n')
            print('=-' * 20)

            return mestre_encontrado

#[RANDOMIZACAO DA EQUIPE INICIAL]
def definir_equipe_inicial() -> str:
    """Sorteia aleatoriamente qual equipe iniciará a partida.

    Returns:
        O nome da equipe sorteada ("VERMELHA" ou "AZUL").
    """
    #Sorteia qual equipe ira começar a partida
    equipe_inicial = random.choice(["VERMELHA", "AZUL"])

    cor_equipe = definir_cor(equipe_inicial)

    print(f'\nA equipe que começa é: {cor_equipe}{equipe_inicial}{RESET}\n')
    print('=-' * 20)

    return equipe_inicial