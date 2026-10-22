def conceito(nota):
    if 0 > nota or nota > 10:
        print('Nota inválida!!')
    elif 9 <= nota:
        print(f'Sua nota foi {nota} e você recebeu: A')

    elif 7 <= nota:
        print(f'Sua nota foi {nota} e você recebeu: B')

    elif 5 <= nota:
        print(f'Sua nota foi {nota} e você recebeu: C')

    else:
        print(f'Sua nota foi {nota} e você recebeu: D')

conceito(-1)
conceito(9.8)
conceito(8.9)
conceito(9)
conceito(11)
conceito(4)
conceito(0)
conceito(10)