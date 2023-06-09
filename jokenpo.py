from random import randint
from time import sleep

itens = ('Pedra ✊', 'Papel 🖐️', 'Tesoura ✌')

print('Preparado para o jogo de JO KEN PO...\n')
print('''Suas opções: \n
[0] = PEDRA ✊
[1] = PAPEL 🖐️
[2] = TESOURA ✌ \n''')

while True:
    computador = randint(0, 2)

    while True:
        try:
            jogador = int(input('Qual é a sua jogada? '))
            if jogador < 0 or jogador > 2:
                print('Jogada inválida! Por favor, escolha uma opção válida (0, 1 ou 2).\n')
            else:
                break
        except ValueError:
            print('Jogada inválida! Por favor, escolha uma opção válida (0, 1 ou 2).\n')

    print('JO')
    sleep(0.5)
    print('KEM')
    sleep(0.5)
    print('PO')

    print('-=' * 14)
    print('Você jogou: {}'.format(itens[jogador]))
    print('Computador jogou: {}'.format(itens[computador]))
    print('-=' * 14)

    if computador == jogador:
        print('EMPATE')
    elif (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):
        print('Você venceu ✅')
    else:
        print('Você perdeu ❌')

    jogar_novamente = input('Deseja jogar novamente? S para sim e N para não(S/N) ')
    if jogar_novamente.upper() != 'S':
        break

print('Obrigado por jogar!')
