import os
from palavras import lista_palavras, sortear_palavras
from tabuleiro import estrutura_tabuleiro, gerar_categorias, exibir_tabuleiro
from tabuleiro import revelar_palavra
from jogo import trocar_turno, verificar_palpite, verificar_vitoria, menu_inicial, limpar_tela

def main():
    print("=" * 40)
    print("          CODENAMES - PYTHON")
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

    palavras_partida = sortear_palavras(lista_palavras, 25)
    categorias_geradas = gerar_categorias(False, True)

    tabuleiro = estrutura_tabuleiro(palavras_partida, categorias_geradas)

    equipe_atual = "vermelho"

    jogo_ativo = True

    while jogo_ativo:
        limpar_tela(os.name)

        print("=" * 55)
        print("      ATENÇÃO: SOMENTE OS MESTRES PODEM OLHAR!")
        print("=" * 55)

        input("\nQuando somente os mestres estiverem olhando, pressione Enter...")

        limpar_tela(os.name)

        print(f"\n--- MAPA DOS MESTRES ---")
        exibir_tabuleiro(tabuleiro, modo_mestre=True)

        print(f"\nTurno da equipe {equipe_atual.upper()}.")

        pista = input(f"Mestre da equipe {equipe_atual.upper()}, digite a pista: ").strip()

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
        print("JOGADORES PODEM OLHAR")
        print("=" * 55)

        print(f"\nEquipe da vez: {equipe_atual.upper()}")
        print(f"Pista: {pista.upper()} | Quantidade: {quantidade}")

        print("\n--- TABULEIRO ---")
        exibir_tabuleiro(tabuleiro, modo_mestre=False)

        while palpites_restantes > 0 and jogo_ativo:
            print(f"\nPista: {pista.upper()} | Palpites restantes: {palpites_restantes}")

            palpite = input("Digite uma palavra ou 'passar' para encerrar o turno: ").strip()

            if palpite.lower() == "passar":
                equipe_atual = trocar_turno(equipe_atual)

                print("\nTurno encerrado.")
                print(f"Agora é a vez da equipe {equipe_atual.upper()}.")

                break

            resultado = revelar_palavra(tabuleiro, palpite)
            resultado_palpite = verificar_palpite(resultado, equipe_atual)

            if resultado_palpite == "acerto":
                print(f"\nAcertou uma palavra da equipe {equipe_atual.upper()}!")

                if verificar_vitoria(tabuleiro, equipe_atual):
                    print(f"A equipe {equipe_atual.upper()} venceu!")
                    jogo_ativo = False

                else:
                    palpites_restantes -= 1

                    if palpites_restantes == 0:
                        print("\nLimite de palpites atingido.")

                        equipe_atual = trocar_turno(equipe_atual)

                        print(f"Agora é a vez da equipe {equipe_atual.upper()}.")

                    else:
                        print("A equipe pode continuar jogando.")

            elif resultado_palpite == "fim_turno":
                equipe_adversaria = trocar_turno(equipe_atual)

                if verificar_vitoria(tabuleiro, equipe_adversaria):
                    print(f"\nA última palavra da equipe {equipe_adversaria.upper()} foi revelada!")
                    print(f"A equipe {equipe_adversaria.upper()} venceu!")

                    jogo_ativo = False

                else:
                    print("\nFim do turno.")

                    equipe_atual = equipe_adversaria

                    print(
                        f"Agora é a vez da equipe {equipe_atual.upper()}.")

                break

            elif resultado_palpite == "derrota":
                print(f"\nA equipe {equipe_atual.upper()} encontrou o ASSASSINO!")
                print("Fim de jogo.")

                jogo_ativo = False

            elif resultado_palpite == "invalido":
                print(f"\n{resultado}")

            exibir_tabuleiro(tabuleiro, modo_mestre=False)

if __name__ == "__main__": #mais seguro de rodar o main para em caso de import do main ele nao rodar automaticamente, mas sim apenas quando for chamado diretamente
    main()
