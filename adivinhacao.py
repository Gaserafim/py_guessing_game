import random
import time

def iniciaJogo():
    print('Estou pensando em um número...')

    num_aleatorio = random.randint(1, 10)

    time.sleep(2)
    print('Pronto! Pensei em um número entre 1 e 10.')
    time.sleep(1)
    print('Você terá 5 chances...')
    time.sleep(1)
    print('Pode tentar adivinhar!')
    time.sleep(1)

    num_usuario = int(input('Digite o seu número: '))
    num_tentativas = 1

    while num_usuario != num_aleatorio:
        print('Que pena, você errou! Tente novamente.')
        num_usuario = int(input('Digite o seu número: '))
        num_tentativas += 1
        
        if num_usuario == num_aleatorio:
            print(f'Parabéns, você adivinhou! O número que eu estava pensando era exatamente o {num_aleatorio}.')
            break

        if num_tentativas >= 5:
            print('Você perdeu!\nNúmero de tentativas excedido.')
            break

print('#' * 32)
print('Bem-vindo ao jogo de adivinhação')
print('#' * 32)

time.sleep(2)

restart = 'S'
while restart == 'S':
    iniciaJogo()
    restart = str(input('Você gostaria de jogar de novo? [S/N]: ')).upper()
print('Obrigado por jogar!')