# Codenames Python

Implementação do jogo **Codenames** desenvolvida em Python como projeto acadêmico em grupo.

## 👥 Equipe

* Gabriel Ricardo
* Pedro Limeis
* Ana Clara Magalhães

## 🎯 Objetivo

Desenvolver uma versão funcional do jogo **Codenames** utilizando Python, aplicando conceitos de:

* lógica de programação;
* funções;
* estruturas condicionais;
* estruturas de repetição;
* listas e dicionários;
* modularização de código;
* validação de entradas;
* organização de projeto;
* versionamento com Git;
* colaboração utilizando GitHub.

O projeto será desenvolvido de forma incremental, priorizando inicialmente o funcionamento das principais regras do jogo.

## 🎮 Sobre o jogo

Codenames é um jogo de palavras disputado entre duas equipes.

Durante a partida, palavras são distribuídas em um tabuleiro e associadas secretamente a diferentes categorias:

* equipe vermelha;
* equipe azul;
* palavras neutras;
* assassino.

O mestre de cada equipe fornece pistas relacionadas às palavras pertencentes ao seu time.

Os jogadores devem utilizar essas pistas para descobrir corretamente suas palavras, evitando palavras da equipe adversária, palavras neutras e principalmente o assassino.

## ⚙️ Funcionalidades planejadas

O projeto deverá possuir inicialmente:

* criação do tabuleiro;
* seleção aleatória das palavras;
* divisão das palavras entre as equipes;
* identificação de palavras neutras;
* definição da palavra assassina;
* gerenciamento das equipes;
* controle dos turnos;
* registro das pistas;
* processamento dos palpites;
* validação das escolhas;
* atualização do estado do tabuleiro;
* condição de vitória;
* condição de derrota ao escolher o assassino;
* possibilidade de iniciar uma nova partida.

## 🛠 Tecnologias

* Python
* Git
* GitHub

## 📁 Estrutura planejada

A estrutura será definida conforme o desenvolvimento avançar, evitando criar módulos desnecessários antes de existir uma responsabilidade clara para eles.

Estrutura inicial prevista:

```text
Codenames-Python/
│
├── src/
│   └── main.py
│
├── tests/
│
├── docs/
│
├── .gitignore
├── LICENSE
└── README.md
```

Novos módulos poderão ser adicionados dentro de `src/` conforme as funcionalidades forem implementadas.

## 🌿 Organização das branches

O desenvolvimento será feito utilizando branches separadas para cada funcionalidade.

Branch principal:

```text
main
```

Branch de integração:

```text
develop
```

Exemplos de branches de desenvolvimento:

```text
feature/criacao-tabuleiro
feature/equipes
feature/sistema-turnos
feature/palpites
```

Fluxo esperado:

```text
feature/* → develop → main
```

A branch `develop` será utilizada para reunir e testar as funcionalidades antes da integração com a `main`.

## 📝 Padrão de commits

Sempre que possível, serão utilizados commits curtos e descritivos.

Exemplos:

```text
feat: implementa criação do tabuleiro
feat: adiciona sistema de equipes
fix: corrige troca de turno
fix: valida palavra já escolhida
refactor: separa validação de palpites
docs: atualiza README
```

## ▶️ Como executar

Após a implementação inicial do projeto:

```bash
git clone https://github.com/gabriel-ricardo-ADS/Codenames-Python.git
```

Entre na pasta do projeto:

```bash
cd Codenames-Python
```

Execute o programa:

```bash
python src/main.py
```

> Os comandos poderão ser atualizados conforme a estrutura definitiva do projeto for criada.

## 🚧 Status do projeto

**Em desenvolvimento.**

Atualmente o projeto está em sua fase inicial de organização e definição da estrutura.

O primeiro objetivo será construir o núcleo funcional do Codenames antes da implementação de funcionalidades adicionais.

## 📌 Prioridades de desenvolvimento

1. Estrutura inicial do projeto
2. Banco de palavras
3. Criação do tabuleiro
4. Distribuição das palavras entre equipes, neutras e assassino
5. Equipes e jogadores
6. Sistema de turnos
7. Pistas
8. Palpites
9. Condições de vitória e derrota
10. Validações e testes
11. Melhorias e funcionalidades adicionais

## 📄 Licença

Este projeto utiliza a licença disponível no arquivo `LICENSE`.
