def estatistica(lista):
    soma = 0
    if len(lista) == 0:
        print('Lista inválida!!')

    else:
        for s in lista:
            soma += s
        maior = 0
        menor = 0
        for pos, m in enumerate(lista):
            if pos == 0:
                maior = m
                menor = m

            if m > maior:
                maior = m

            if m < menor:
                menor = m


        print(f'A soma entre os números é: {soma}')
        print(f'A média da soma é: {soma / len(lista)}')
        print(f'O maior número da lista é: {maior}')
        print(f'O menor número da lista é: {menor}')

estatistica([4, 8, 6])
estatistica([])
estatistica([-5, -2 , -9])
estatistica([7])