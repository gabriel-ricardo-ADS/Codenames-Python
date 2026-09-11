import os

from palavras import lista_palavras, sortear_palavras
from tabuleiro import estrutura_tabuleiro, gerar_categorias, exibir_tabuleiro, revelar_palavra
from jogo import trocar_turno, verificar_palpite, verificar_vitoria, menu_inicial, limpar_tela
from jogadores import cadastrar_jogadores, dividir_equipes, escolher_mestre, definir_equipe_inicial, VERDE, VERMELHO, AZUL, RESET


def formatar_equipe(equipe: str) -> str:
    """Formata o nome da equipe com a respectiva cor ANSI (vermelho ou azul).

    Args:
        equipe: O nome da equipe ("vermelho", "VERMELHA", "azul", etc.).

    Returns:
        O nome da equipe formatado em maiúsculas acompanhado de sua cor ANSI.
    """
    if equipe.upper() in ["VERMELHA", "VERMELHO"]:
        return f"{VERMELHO}{equipe.upper()}{RESET}"
    elif equipe.upper() in ["AZUL"]:
        return f"{AZUL}{equipe.upper()}{RESET}"
    return equipe.upper()


def main() -> None:
    """Função principal que executa o fluxo do jogo Codenames."""
    print("=" * 40)
    print(f"          CODENAMES - {VERDE}PYTHON{RESET}")
    print("=" * 40)

    print("\nBem-vindo ao Codenames!")

    opcao = menu_inicial(["1", "2", "0"])

    while opcao == "2":
        print("\n=== COMO JOGAR ===")
        print("Duas equipes disputam para descobrir suas palavras.")
        print("O mestre fornece uma pista e uma quantidade.")
        print("A equipe tenta encontrar as palavras relacionadas à pista.")
        print("Palavras neutras ou adversárias encerram o turno.")
        print("Quem revelar o assassino perde imediatamente.")

        opcao = menu_inicial(["1", "2", "0"])

    if opcao == "0":
        print("\nJogo encerrado.")
        return

    jogadores = cadastrar_jogadores()
    equipe_vermelha, equipe_azul = dividir_equipes(jogadores)
    mestre_vermelho = escolher_mestre(equipe_vermelha, "VERMELHA")
    mestre_azul = escolher_mestre(equipe_azul, "AZUL")
    input("\nMestres-espiões definidos! Pressione Enter para continuar...")
    equipe_inicial = definir_equipe_inicial()
    palavras_partida = sortear_palavras(lista_palavras, 25)

    if equipe_inicial == "VERMELHA":
        categorias_geradas = gerar_categorias(False, True)
        equipe_atual = "vermelho"
    else:
        categorias_geradas = gerar_categorias(True, False)
        equipe_atual = "azul"

    tabuleiro = estrutura_tabuleiro(palavras_partida, categorias_geradas)

    jogo_ativo = True

    while jogo_ativo:
        limpar_tela(os.name)

        print("=" * 55)
        print("      ATENÇÃO: SOMENTE OS MESTRES PODEM OLHAR!")
        print("=" * 55)

        input("\nQuando somente os mestres estiverem olhando, pressione Enter...")

        limpar_tela(os.name)

        print("\n--- MAPA DOS MESTRES ---")
        exibir_tabuleiro(tabuleiro, modo_mestre=True)

        print(f"\nTurno da equipe {formatar_equipe(equipe_atual)}.")

        pista = input(f"Mestre da equipe {formatar_equipe(equipe_atual)}, digite a pista: ").strip()

        while True:
            try:
                quantidade = int(input("Quantidade de palavras relacionadas à pista: "))

                if quantidade <= 0:
                    print("Digite uma quantidade maior que zero.")
                else:
                    break

            except ValueError:
                print("Digite apenas números.")

        palpites_restantes = quantidade + 1

        input("\nMestres, pressionem Enter quando estiverem prontos para entregar a tela aos jogadores...")

        limpar_tela(os.name)

        print("=" * 55)
        print("              JOGADORES PODEM OLHAR")
        print("=" * 55)

        print(f"\nEquipe da vez: {formatar_equipe(equipe_atual)}")
        print(f"Pista: {pista.upper()} | Quantidade: {quantidade}")

        print("\n--- TABULEIRO ---")
        exibir_tabuleiro(tabuleiro, modo_mestre=False)

        while palpites_restantes > 0 and jogo_ativo:
            print(f"\nPista: {pista.upper()} | Palpites restantes: {palpites_restantes}")

            palpite = input("Digite uma palavra ou 'passar' para encerrar o turno: ").strip()

            if palpite.lower() == "passar":
                equipe_atual = trocar_turno(equipe_atual)

                print("\nTurno encerrado.")
                print(f"Agora é a vez da equipe {formatar_equipe(equipe_atual)}.")

                break

            resultado = revelar_palavra(tabuleiro, palpite)
            resultado_palpite = verificar_palpite(resultado, equipe_atual)

            if resultado_palpite != "invalido":
                print("\n--- TABULEIRO ATUALIZADO ---")
                exibir_tabuleiro(tabuleiro, modo_mestre=False)

            if resultado_palpite == "acerto":
                print(f"\nAcertou uma palavra da equipe {formatar_equipe(equipe_atual)}!")

                if verificar_vitoria(tabuleiro, equipe_atual):
                    print(f"A equipe {formatar_equipe(equipe_atual)} venceu!")
                    jogo_ativo = False

                else:
                    palpites_restantes -= 1

                    if palpites_restantes == 0:
                        print("\nLimite de palpites atingido.")

                        equipe_atual = trocar_turno(equipe_atual)

                        print(f"Agora é a vez da equipe {formatar_equipe(equipe_atual)}.")

                        input("\nPressione Enter para continuar para o próximo turno...")

                    else:
                        print("A equipe pode continuar jogando.")

            elif resultado_palpite == "fim_turno":
                equipe_adversaria = trocar_turno(equipe_atual)

                if verificar_vitoria(tabuleiro, equipe_adversaria):
                    print(f"\nA última palavra da equipe {formatar_equipe(equipe_adversaria)} foi revelada!")
                    print(f"A equipe {formatar_equipe(equipe_adversaria)} venceu!")

                    jogo_ativo = False

                else:
                    print("\nFim do turno.")

                    equipe_atual = equipe_adversaria

                    print(f"Agora é a vez da equipe {formatar_equipe(equipe_atual)}.")

                    input("\nPressione Enter para continuar para o próximo turno...")

                break

            elif resultado_palpite == "derrota":
                print(f"\nA equipe {formatar_equipe(equipe_atual)} encontrou o ASSASSINO!")
                print("Fim de jogo.")

                jogo_ativo = False

            elif resultado_palpite == "invalido":
                print(f"\n{resultado}")
                
if __name__ == "__main__":
    main()