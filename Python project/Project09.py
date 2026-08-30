from random import randint
from time import sleep
resultado = {}
for d in range(1, 5):
    dado = randint(1,6)
    print(f'{d}o jogador Tirou: {dado}')
    resultado[f'jogador{d}'] = dado

sleep(0.5)
ordenado = sorted(resultado.items(),key=lambda item: item[1], reverse=True)
print('-=' * 20)
print('          RANKING DO SORTEIO')
print('-=' * 20)
cont = 0
for o in ordenado:
    cont += 1
    print(f'{cont}o lugar: {o[0]} : {o[1]}')
    sleep(0.5)
