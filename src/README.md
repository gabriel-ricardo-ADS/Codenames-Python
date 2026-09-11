# Codenames Python

Implementação do jogo **Codenames** desenvolvida em Python como projeto acadêmico da disciplina de **Computational Thinking Using Python** da FIAP.

O projeto recria a dinâmica principal do Codenames para execução diretamente pelo terminal, utilizando conceitos fundamentais de lógica de programação, modularização e estruturas de dados em Python.

---

## 👥 Equipe

- Ana Clara Pereira de Magalhães — RM560871
- Gabriel Ricardo Gomes Lima — RM572279
- Pedro Henrique de Lima Reis — RM569178

---

## 🎯 Objetivo

Desenvolver uma versão funcional do jogo **Codenames** utilizando Python, aplicando conceitos estudados durante a disciplina, como:

- lógica de programação;
- funções;
- parâmetros e retornos;
- estruturas condicionais;
- estruturas de repetição;
- listas;
- dicionários;
- modularização;
- tratamento e validação de entradas;
- organização de código;
- Git e GitHub;
- desenvolvimento colaborativo.

---

## 🎮 Sobre o jogo

Codenames é um jogo de associação de palavras disputado entre duas equipes:

- 🔴 Equipe Vermelha
- 🔵 Equipe Azul

Cada equipe possui um **Mestre-Espião**, responsável por fornecer pistas para os demais jogadores.

Durante a partida, são sorteadas **25 palavras**, organizadas em um tabuleiro 5x5.

Cada palavra pertence secretamente a uma das seguintes categorias:

- Equipe Vermelha;
- Equipe Azul;
- Neutra;
- Assassino.

Os Mestres-Espiões conseguem visualizar a identidade de todas as cartas, enquanto os demais jogadores visualizam apenas as palavras.

---

## 🕵️ Como funciona

Em cada turno, o Mestre-Espião da equipe fornece:

```text
PISTA + QUANTIDADE
```

Exemplo:

```text
OCEANO 3
```

A pista deve possuir relação com uma ou mais palavras presentes no tabuleiro.

A equipe então tenta descobrir quais palavras estão relacionadas à pista fornecida.

Ao escolher uma palavra:

- se pertencer à própria equipe, o time pode continuar jogando;
- se pertencer à equipe adversária, o turno termina;
- se for neutra, o turno termina;
- se for o assassino, a equipe perde imediatamente;
- se todas as palavras de uma equipe forem reveladas, ela vence a partida.

Os jogadores também podem utilizar a opção:

```text
passar
```

para encerrar voluntariamente o turno.

---

## ✅ Funcionalidades implementadas

- cadastro de 4 a 10 jogadores;
- validação dos nomes dos jogadores;
- divisão dos jogadores entre as equipes;
- escolha dos Mestres-Espiões;
- sorteio da equipe inicial;
- sorteio aleatório de 25 palavras;
- geração das categorias das cartas;
- tabuleiro 5x5;
- visão normal dos jogadores;
- mapa secreto dos Mestres-Espiões;
- diferenciação das cartas por cores;
- identificação permanente das cartas já reveladas;
- sistema de pistas;
- quantidade de palavras associadas à pista;
- sistema de palpites;
- controle de palpites restantes;
- opção de passar o turno;
- alternância automática de turnos;
- tratamento de palavra neutra;
- tratamento de palavra adversária;
- derrota ao selecionar o assassino;
- condição de vitória;
- validação de palavras inexistentes;
- validação de palavras já reveladas;
- limpeza do terminal entre a visão dos Mestres e dos jogadores.

---

## 🛠 Tecnologias utilizadas

- Python
- Git
- GitHub
- Visual Studio Code

O projeto utiliza apenas recursos da biblioteca padrão do Python, sem necessidade de instalar bibliotecas externas.

---

## 📁 Estrutura do projeto

```text
Codenames-Python/
│
├── src/
│   ├── main.py
│   ├── jogo.py
│   ├── jogadores.py
│   ├── palavras.py
│   └── tabuleiro.py
│
├── docs/
│
├── .gitignore
├── LICENSE
└── README.md
```

### Principais arquivos

`main.py`  
Responsável por integrar os módulos e controlar o fluxo principal da partida.

`jogo.py`  
Contém funções relacionadas às regras, turnos, palpites e condições de vitória.

`jogadores.py`  
Responsável pelo cadastro, divisão das equipes, escolha dos Mestres-Espiões e sorteio da equipe inicial.

`palavras.py`  
Contém o banco de palavras utilizado nas partidas e o sorteio das palavras.

`tabuleiro.py`  
Responsável pela criação, exibição e atualização do tabuleiro.

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/gabriel-ricardo-ADS/Codenames-Python.git
```

### 2. Entre na pasta

```bash
cd Codenames-Python
```

### 3. Execute o jogo

```bash
python src/main.py
```

Também é possível abrir o projeto no Visual Studio Code:

```bash
code .
```

e executar o arquivo:

```text
src/main.py
```

---

## 🎲 Requisitos para jogar

- Python 3 instalado;
- terminal compatível com cores ANSI;
- mínimo de 4 jogadores;
- máximo de 10 jogadores.

Não é necessário instalar dependências externas.

---

## 🌿 Git Flow

O desenvolvimento do projeto foi realizado utilizando branches para separar funcionalidades.

```text
feature/* → develop → main
```

### Branches

`main`  
Versão estável do projeto.

`develop`  
Branch utilizada para integração das funcionalidades.

`feature/*`  
Branches utilizadas para desenvolvimento de funcionalidades específicas.

---

## 📝 Padrão de commits

Foram utilizados commits curtos e descritivos.

Exemplos:

```text
feat: implementa criação do tabuleiro
feat: adiciona sistema de equipes
fix: corrige troca de turno
fix: valida palavra já escolhida
refactor: organiza funções do jogo
docs: atualiza documentação
```

---

## 📄 Documentação

A documentação acadêmica completa do projeto apresenta:

- identificação da equipe;
- funcionamento do Codenames;
- principais regras;
- instruções para execução do projeto.

### Documento completo

> 📎 **[Clique aqui para acessar a documentação completa](docs/documentacao-codenames.pdf)**

---

## 🔗 Links

- Repositório: https://github.com/gabriel-ricardo-ADS/Codenames-Python
- Codenames: https://codenames.game/

---

## 📚 Disciplina

**Computational Thinking Using Python**

Curso: Análise e Desenvolvimento de Sistemas — FIAP  
Turma: 1TDSPF  
Professor: Fernando Luiz de Almeida

---

## 📄 Licença

Este projeto utiliza a licença disponível no arquivo `LICENSE`.
