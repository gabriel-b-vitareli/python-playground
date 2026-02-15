from random import randint
print('\033[1;34mIrei pensar em um numero entre 1 e 5. Seu objetivo é tentar adivinhar qual é esse número que estou pensando.\033[m')
print('\033[1;34mDigite 0 para encerrar.\033[m')
random = 0
acertos = 0
errados = 0
while True:
    random = randint(1, 5)
    escolha = int(input('\033[1;36mTente adivinhar: \033[m'))
    if escolha == 0:
        print(f'\033[1;36mJogo encerrado. Suas estatísticas foram:\nVezes jogadas: {acertos + errados}\n\033[m\033[1;32mAcertos: {acertos}\033[m\n\033[1;31mTentaivas erradas: {errados}.\033[m')
        break
    elif random == escolha:
        print('\033[1;32mVocê acertou!\033[m')
        acertos += 1
    elif escolha != random and escolha < 6:
        print(f'\033[1;31mVocê errou. Eu estava pensando em {random}. Irei pensar em outro número.\033[m')
        errados += 1
    else:
        print('Você escolheu um número inválido. Tente novamente.')
