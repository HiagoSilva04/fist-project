lista = list()
armazenar = list()
while True:
    nome_aluno = input('Nome: ')
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    lista.append(nome_aluno)
    lista.append(nota1)
    lista.append(nota2)
    armazenar.append(lista[:])
    lista.clear()
    escolha = input('Quer contnuar[S/N]: ').upper()
    if escolha == 'N':
        break

print('-=' * 30)
print(f'{'Pos':<5}' f'{'Nome':<10}' f'{'Média':<15}')
print('_' * 30)
for pos , n in enumerate(armazenar):
    print(f'{pos:<5}' f'{n[0]:<10}' f'{(n[1] + n[2]) /2 :<20}' )
print('_' * 30)

while True:
     aluno = int(input('De quem vc deseja ver a nota(999 para parar): '))

     while (aluno < 0 or aluno >= len(armazenar)) and aluno != 999:
        aluno = int(input('Tente novamente aluno não encontrado: '))

     if aluno != 999:
        escolha_usuario = armazenar[aluno]
        print(f'As notas do {escolha_usuario[0]} são: {[escolha_usuario[1], escolha_usuario[2]]}')
        print('_' * 30)
     else:
         print('Até mais!!!')
         break