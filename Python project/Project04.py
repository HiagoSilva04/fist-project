nome_usuario = 'Hiago'
senha_usuario = 1234
cont = 0
while True:
    nome = input('Dígite o nome de usuário: ').capitalize()
    if nome == nome_usuario:
        print('Nome correto...Agora dígite a senha!!')
        break
    elif nome != 'Hiago':
        print('Nome incorreto....tente novamente!!')

senha = 0 
while True:
    cont += 1 
    senha = int(input('Dígite a senha: '))
    if senha == senha_usuario:
        print('Acesso ao sistema!!')
        break

    elif senha != 1234:
        print('Senha incorreta....Tente novamente!!')

   
    if cont == 4:
        print('Limite de tenteativas alcançadas...tente mais tarde!!')
        break
