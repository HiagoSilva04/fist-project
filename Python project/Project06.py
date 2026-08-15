pares = list()
impares = list()
lista = list()
lista.append(pares)
lista.append(impares)
for c in range(7):
    numeros = int(input('Dígite um número: '))
    if numeros % 2 == 0:
        lista[0].append(numeros)
    else:
        lista[1].append(numeros)

print(f'Pares: {sorted(lista[0])}')
print(f'Ímpares: {sorted(lista[1])}')
