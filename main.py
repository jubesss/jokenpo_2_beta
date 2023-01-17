from random import randint
itens = ("FOGO", "ÁGUA" ,"PLANTA")
computador = randint(0, 2)
print("=-_-=" *9)
print('\033[1;34mBEM-VINDO AO JOKENPO 2!\033[m')
nome = input('Primeiro, qual é o seu nome? ')
print("=-_-=" *9)
print(nome,''', suas opções são:
[0] FOGO
[1] ÁGUA
[2] PLANTA''')
jogador = int(input("Digite o número da sua jogada! -> "))
print("=-_-=" *9)
print("jogador jogou {}".format(itens[jogador]))
print("computador jogou {}".format(itens[computador]))
print("=-_-=" *9)

if jogador == computador:
    print('\033[0;34mempatou!\033[m')
elif jogador == 0 and computador == 1:
    print('a água apagou o fogo!')
    print('\033[0;31mvocê perdeu...\033[m')
    print("=-_-=" * 9)
elif jogador == 1 and computador == 0:
    print('a água apagou o fogo')
    print('\033[0;32mvocê venceu!\033[m')
    print("=-_-=" * 9)
elif jogador == 2 and computador == 1:
    print('a planta resistiu a água!')
    print('\033[0;32mvocê venceu!\033[m')
    print("=-_-=" * 9)
elif jogador == 1 and computador == 2:
    print('a planta resistiu a água!')
    print('\033[0;31mvocê perdeu...\033[m')
    print("=-_-=" * 9)
elif jogador == 2 and computador == 0:
    print('o fogo queimou a planta!')
    print('\033[0;31mvocê perdeu...\033[m')
    print("=-_-=" * 9)
else:
    print('o fogo queimou a planta!')
    print('\033[0;32mVocê venceu!\033[m')
    print("=-_-=" * 9)
