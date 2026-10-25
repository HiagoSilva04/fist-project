def palindromo(texto : str):
    novo = ''
    texto = texto.lower()
    for p in texto:
        novo = p + novo
    if novo == texto:
        print('É palíndromo!')
    else:
        print('Não é palíndromo!')



palindromo('Arara')
palindromo('cAsa')
palindromo('Asa')