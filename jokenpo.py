from random import randint #Deixar o código randomico
from time import sleep #Marcador de tempo para as strings JO KEN PO

itens = ('Pedra ✊', 'Papel 🖐️ ', 'Tesoura ✌')

computador = randint(0, 2)

print('Preparado para o jogo de JO KEN PO...\n')
print('''Suas opções: \n
[0] = PEDRA ✊
[1] = PAPEL 🖐️
[2] = TESOURA ✌ \n''')

jogador = int(input('Qual é a sua jogada ❓ \n'))

print('JO')
sleep(0.5)
print('kEN')
sleep(0.5)
print('PO')

print('-=' * 14)
print('você jogou {}'.format(itens[jogador]))
print('Computador jogou {}'.format(itens[computador]))
print('-=' * 14)

if computador == 0: #computador jogou PEDRA

    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('Você venceu ✅')
        
    elif jogador == 2:
        print('Você perdeu ❌')

    else:
        print('Jogada inválida! ⚠️')

elif computador == 1: #computador jogou PAPEL

    if jogador == 0:
        print('Você perdeu ❌')

    elif jogador == 1:
        print('EMPATE')
        
    elif jogador == 2:
        print('Você venceu ✅')

    else:
        print('Jogada inválida! ⚠️')
            
elif computador == 2: #computador jogou TESOURA

    if jogador == 0:
        print('Você venceu ✅')

    elif jogador == 1:
        print('Você perdeu ❌')
        
    elif jogador == 2:
        print('EMPATE')

    else:
        print('Jogada inválida! ⚠️') 
