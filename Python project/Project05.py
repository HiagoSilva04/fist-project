import emoji
limite = 300
soma = 0
while True:
    produto = input('Nome do produto: ').upper()
    if produto == 'NADA':
        break
    else:
        valor = int(input('Valor: '))
        soma += valor

if soma <= limite:
    resultado = emoji.emojize('Saldo positivo: :green_circle:')
if soma > limite:
    resultado = emoji.emojize('Saldo negativo: :red_circle:')

print(f'O valor total dos produtos foi{soma}')
print(resultado)
