from time import sleep
def maior(*num):
        print('-=' * 30)
        quantidade = len(num)
        if len(num) == 0:
            print(f'Foram informados {quantidade} valores no total.')
            print(f'E o maior número entre eles é: 0.')
        else:
            print('Analisando os valores...')

            for m in num:
                print(f'{m}', end=' ')
                sleep(0.5)
            print(f'Foram informados {quantidade} valores no total.')
            print(f'E o maior entre eles é: {max(num)}.')



maior(2, 4, 5, 8, 3)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()