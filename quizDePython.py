
from rich import print
from rich.traceback import install
from rich.table import Table
from rich import box
import random

install()

# Quiz de Conhecimentos em Python


def boas_vindas():
    print("\n[bold green]Seja bem-vindo(a) ao Quiz de Conhecimentos em Python![/] :snake:")

    print("\n[bold blue]O objetivo deste projeto é desenvolver um jogo de perguntas e respostas utilizando a linguagem Python, com o intuito de colocar em prática os conhecimentos adquiridos durante o curso. O programa consiste em apresentar perguntas de múltipla escolha, permitindo que o jogador selecione uma das alternativas disponíveis e receba imediatamente o resultado de sua resposta. Durante o desenvolvimento, serão utilizados conceitos fundamentais de programação, como listas, dicionários, funções, estruturas condicionais e de repetição, além da validação de dados. Ao final de cada partida, o sistema apresentará a quantidade de acertos, erros e a pontuação total do jogador. Dessa forma, o projeto busca desenvolver o raciocínio lógico, aprimorar as habilidades de programação e demonstrar, na prática, a aplicação dos conceitos estudados.[/]")

    print("\n" + "-" * 80)

    print("\n[bold yellow]REGRAS DO QUIZ[/]")
    print("[white]• Serão apresentadas 5 perguntas aleatórias.[/]")
    print("[white]• Cada pergunta possui 4 alternativas.[/]")
    print("[white]• Escolha uma resposta entre A, B, C ou D.[/]")
    print("[white]• Cada resposta correta vale 1 ponto.[/]")
    print("[white]• Não será permitido repetir perguntas.[/]")

    print("\n" + "-" * 80)


# Banco de perguntas

perguntas = [
    {
        "id": 1,
        "enunciado": "Qual função é utilizada para exibir informações na tela?",
        "alternativas": [
            "input()",
            "print()",
            "int()",
            "str()"
        ],
        "resposta_correta": 2
    },
    {
        "id": 2,
        "enunciado": "Qual comando é utilizado para receber dados do usuário?",
        "alternativas": [
            "print()",
            "float()",
            "input()",
            "type()"
        ],
        "resposta_correta": 3
    },
    {
        "id": 3,
        "enunciado": "Qual estrutura é utilizada para criar uma condição em Python?",
        "alternativas": [
            "if",
            "for",
            "def",
            "import"
        ],
        "resposta_correta": 1
    },
    {
        "id": 4,
        "enunciado": "Qual estrutura é utilizada para repetir um bloco de código enquanto uma condição for verdadeira?",
        "alternativas": [
            "if",
            "else",
            "while",
            "return"
        ],
        "resposta_correta": 3
    },
    {
        "id": 5,
        "enunciado": "Qual símbolo é utilizado para realizar uma divisão inteira?",
        "alternativas": [
            "/",
            "%",
            "**",
            "//"
        ],
        "resposta_correta": 4
    },
    {
        "id": 6,
        "enunciado": "Qual função converte um valor para número inteiro?",
        "alternativas": [
            "str()",
            "int()",
            "float()",
            "input()"
        ],
        "resposta_correta": 2
    },
    {
        "id": 7,
        "enunciado": "Qual palavra-chave é utilizada para definir uma função em Python?",
        "alternativas": [
            "class",
            "function",
            "def",
            "return"
        ],
        "resposta_correta": 3
    },
    {
        "id": 8,
        "enunciado": "Qual estrutura de dados armazena informações em pares de chave e valor?",
        "alternativas": [
            "Lista",
            "Tupla",
            "Conjunto",
            "Dicionário"
        ],
        "resposta_correta": 4
    },
    {
        "id": 9,
        "enunciado": "Qual biblioteca permite gerar números aleatórios em Python?",
        "alternativas": [
            "random",
            "math",
            "time",
            "os"
        ],
        "resposta_correta": 1
    },
    {
        "id": 10,
        "enunciado": "Qual método é utilizado para adicionar um elemento ao final de uma lista?",
        "alternativas": [
            "remove()",
            "append()",
            "clear()",
            "pop()"
        ],
        "resposta_correta": 2
    }
]


# Função responsável por executar o quiz

def aplicar_quiz():

    perguntas_sorteadas = random.sample(perguntas, 5)

    acertos = 0

    alternativas = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4
    }

    for numero, pergunta in enumerate(perguntas_sorteadas, start=1):

        print(f"\n[bold cyan]PERGUNTA {numero}/5[/]")

        print(f"\n[bold white]{pergunta['enunciado']}[/]\n")

        for indice, alternativa in enumerate(pergunta["alternativas"], start=1):
            letra = chr(96 + indice)
            print(f"[yellow]{letra.upper()})[/] {alternativa}")

        # Validação da resposta

        while True:

            print("\n[bold green]Sua resposta:[/] ", end="")

            resposta = input().strip().lower()

            if resposta in alternativas:
                break

            print("[bold red]Opção inválida! Digite A, B, C ou D.[/]")

        # Verificação da resposta

        if alternativas[resposta] == pergunta["resposta_correta"]:

            print("\n[bold green]Resposta correta! Muito bem![/] :white_check_mark:")
            acertos += 1

        else:

            correta = pergunta["resposta_correta"]
            letra_correta = chr(96 + correta)

            print("\n[bold red]Resposta incorreta![/] :x:")
            print(f"[yellow]A alternativa correta era: {letra_correta.upper()}[/]")

        print("\n" + "-" * 80)

    return acertos


# Função responsável por apresentar o resultado

def mostrar_resultado(acertos):

    erros = 5 - acertos

    tabela = Table(
        title="RESULTADO FINAL",
        title_style="bold green",
        box=box.ROUNDED
    )

    tabela.add_column("Descrição", style="cyan", justify="center")
    tabela.add_column("Quantidade", style="bold white", justify="center")

    tabela.add_row("Respostas corretas", str(acertos))
    tabela.add_row("Respostas incorretas", str(erros))
    tabela.add_row("Pontuação final", f"{acertos}/5")

    print("\n")
    print(tabela)

    if acertos == 5:
        print("\n[bold green]Excelente! Você acertou todas as perguntas![/] :trophy:")

    elif acertos >= 3:
        print("\n[bold yellow]Muito bem! Você teve um bom desempenho![/]")

    else:
        print("\n[bold red]Continue estudando! Você pode melhorar![/]")


# Execução principal do programa

boas_vindas()

pontuacao = aplicar_quiz()

mostrar_resultado(pontuacao)

print("\n[bold green]Obrigado por participar do Quiz de Conhecimentos em Python![/] :snake:")