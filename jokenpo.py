import random

print('Escolha entre as opções')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
print('4 - Spock')
print('5 - Lagarto')
escolha1 = int(input())

escolha2 = random.randint(1, 5)



if escolha1 == 1:
    if escolha2 == 1:
        print('Empate!!')
    elif escolha2 == 2:
        print('Jogador 1 perdeu!!')
    elif escolha2 == 3:
        print('Jogador 1 venceu!!')
    elif escolha2 == 4:
        print('Jogador 1 perdeu!!')
    else:
        print('Jogador 1 venceu!!')

if escolha1 == 2:
    if escolha2 == 1:
        print('Jogador 1 venceu!!')
    elif escolha2 == 2:
        print('Empate!!')
    elif escolha2 == 3:
        print('Jogador 1 perdeu!!')
    elif escolha2 == 4:
        print('Jogador 1 venceu!!')
    elif escolha2 == 5:
        print('Jogador 1 perdeu!!')

if escolha1 == 3:
    if escolha2 == 1:
        print('Jogador 1 perdeu!!')
    elif escolha2 == 2:
        print('Jogador 1 venceu!!')
    elif escolha2 == 3:
        print('Empate!!')
    elif escolha2 == 4:
        print('Jogador 1 perdeu!!')
    elif escolha2 == 5:
        print('Jogador 1 venceu!!')

if escolha1 == 4:
    if escolha2 == 1:
        print('Jogador 1 venceu!!')
    elif escolha2 == 2:
        print('Jogador 1 perdeu!!')
    elif escolha2 == 3:
        print('Jogador 1 venceu!!')
    elif escolha2 == 4:
        print('Empate!!')
    elif escolha2 == 5:
        print('Jogador 1 perdeu!!')

if escolha1 == 5:
    if escolha2 == 1:
        print('Jogador 1 perdeu!!')
    elif escolha2 == 2:
        print('Jogador 1 venceu!!')
    elif escolha2 == 3:
        print('Jogador 1 perdeu!!')
    elif escolha2 == 4:
        print('Jogador 1 venceu!!')
    elif escolha2 == 5:
        print('Empate!!')