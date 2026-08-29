nome = input('Dígite seu nome: ')
media = float(input('Qual a sua média: '))
situacao = ''
if media <= 5:
    situacao = 'reprovado'
elif 5 < media <= 6.9:
    situacao = 'recuperacao'
elif 6.9 < media <= 10:
    situacao = 'aprovado'

aluno = {'nome': nome,
         'media': media,
         'situacao': situacao}

print(f'     -O aluno é o: {nome}\n'
      f'     -A sua média é de: {media}\n'
      f'     -E sua situação é de: {aluno["situacao"]}')
