from random import choice
lista = ['pedra' , 'papel' , 'tesoura']
while True:
    escolha = int(input('0 = Pedra/1 = Papel/2 = Tesoura: '))
    if escolha in [0 , 1 ,2]:
        break
usuario = lista[escolha]
computer = choice(lista)


if escolha == 0 and computer == 'papel':
    print(f'Vc perdeu jogou {usuario} e o computador jogou {computer}!!')
elif escolha == 1 and computer == 'tesoura':
    print(f'Vc perdeu jogou {usuario} e o computador jogou {computer}!!')
elif escolha == 2 and computer == 'pedra':
    print(f'Vc perdeu jogou {usuario} e o computador jogou {computer}!!')
elif usuario ==  computer:
    print(f'Foi empate vc jogou {usuario} e o computador também!! ')
else:
    print(f'Vc jogou {usuario} e o computador jogou {computer} vc ganhou!!')