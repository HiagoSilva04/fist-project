lista = list()
mais_gordo = list()
cont = 0
resposta = 'S'
while resposta == 'S':
    lista.append(input('Nome: '))
    lista.append(float(input('Peso: ')))
    resposta = input('Quer continuar[S/N]: ').upper()
    mais_gordo.append(lista[:])
    lista.clear()
    cont += 1

    if resposta in 'N':
        break


nome = list()
nome_two = list()
maior = mais_gordo[0][1]
menor = mais_gordo[0][1]
for m in mais_gordo:
    if m[1] > maior:
        maior = m[1]
        nome.clear()
        nome.append(m[0])

    elif m[1] == maior:
        nome.append(m[0])

for md in mais_gordo:
    if md[1] < menor:
        menor = md[1]
        nome_two.clear()
        nome_two.append(md[0])

    elif md[1] == menor:
        nome_two.append(md[0])

print(f'Foram cadastradas {cont} pessoas!')
print(f'O a maior peso é de {maior}. E pertence a {nome}')
print(f'O menor peso foi {menor} e pertence a: {nome_two}')