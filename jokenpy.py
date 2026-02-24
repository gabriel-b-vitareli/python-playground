from random import randint

VERDE = "\033[1;32m"
CIANO = "\033[1;36m"
AMARELO = "\033[1;33m"
VERMELHO = "\033[1;31m"
FIM = "\033[m"

pedra = ['1','pedra','pe']
papel = ['2','papel','pa']
tesoura = ['3', 'tesoura', 't', 'te']

vitorias = 0
empates = 0
derrotas = 0

sequencia = 0
mseq = 0 # Maior sequência de vitórias

print(f'{CIANO}{'-'*40}{FIM}')
print(f'{VERDE} Vamos jogar jokenpô!{FIM}')
print(f'{CIANO}{'-'*40}{FIM}')

while True:
    selecao = input(f'{CIANO} Digite sua escolha: {FIM}').strip().lower()
    computador = randint(1,3)
    if selecao in pedra:
        if computador == 1:
            print(f'{AMARELO}Empatamos! Nós dois escolhemos pedra. {FIM}')
            sequencia = 0
            empates += 1
        elif computador == 2:
            print(f'{VERMELHO}Eu ganhei! Você escolheu pedra, e eu escolhi papel. {FIM}')
            sequencia = 0
            derrotas += 1
        elif computador == 3:
            print(f'{VERDE}Você ganhou! Você escolheu pedra, e eu escolhi tesoura. {FIM}')
            sequencia += 1
            vitorias += 1
            if sequencia > 1:
                print(f'{VERDE}Você já tem uma sequência de {sequencia} vitórias seguidas! Parabéns!{FIM}')
                if sequencia > mseq:
                    mseq = sequencia
    elif selecao in papel:
        if computador == 1:
            print(f'{VERDE}Você ganhou! Você escolheu papel, e eu escolhi pedra. {FIM}')
            sequencia += 1
            vitorias += 1
            if sequencia > 1:
                print(f'{VERDE}Você já tem uma sequência de {sequencia} vitórias seguidas! Parabéns!{FIM}')
                if sequencia > mseq:
                    mseq = sequencia
        elif computador == 2:
            print(f'{AMARELO}Empatamos! Nós dois escolhemos papel. {FIM}')
            sequencia = 0
            empates += 1
        elif computador == 3:
            print(f'{VERMELHO}Eu ganhei! Você escolheu papel, e eu escolhi tesoura. {FIM}')
            sequencia = 0
            derrotas += 1
    elif selecao in tesoura:
        if computador == 1:
            print(f'{VERMELHO}Eu ganhei! Você escolheu tesoura, e eu escolhi pedra. {FIM}')
            sequencia = 0
            derrotas += 1
        elif computador == 2:
            print(f'{VERDE}Você ganhou! Você escolheu tesoura, e eu escolhi papel. {FIM}')
            sequencia += 1
            vitorias += 1
            if sequencia > 1:
                print(f'{VERDE}Você já tem uma sequência de {sequencia} vitórias seguidas! Parabéns!{FIM}')
                if sequencia > mseq:
                    mseq = sequencia
        elif computador == 3:
            print(f'{AMARELO}Empatamos! Nós dois escolhemos tesouras. {FIM}')
            sequencia = 0
            empates += 1
    elif selecao == '0':
        print(f'{CIANO}{'-'*40}{FIM}')
        print(f'{CIANO}Jogo encerrado! Aqui vão suas estatísticas:{FIM}')
        print('')
        print(f'{VERDE}Você ganhou de mim {vitorias} vezes!{FIM}')
        print(f'{AMARELO}Nós empatamos {empates} vezes.{FIM}')
        print(f'{VERMELHO}Eu ganhei de você {derrotas} vezes!{FIM}')
        if mseq > 0:
            print('')
            print(f'{VERDE}Sua maior sequência de vitórias contou com {mseq} vitórias consecutivas! Parabéns!{FIM}')
        print(f'{CIANO}{'-'*40}{FIM}')
        break
    elif selecao not in pedra and selecao not in papel and selecao not in tesoura:
        print(f'{CIANO}Você escolheu uma opção considerada inválida.{FIM}')
    else:
        print(f'{VERMELHO}Um erro desconhecido ocorreu, por favor, tente novamente.{FIM}')
