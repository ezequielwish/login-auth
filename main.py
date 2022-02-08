from database import SqlEmu
import colors


def login():
    global database
    while True:
        user = str(input(colors.color_string('Usuário: ', 'yellow')))
        password = str(input(colors.color_string('Senha: ', 'yellow')))
        check_in_database = database.check_data(id_key=user, data=password, sep='|')
        if check_in_database:
            return True
        else:
            colors.color_print('[X] Usuário ou senha incorretos!', 'red')


def register():
    while True:
        user = str(input(colors.color_string('Novo usuário: ', 'yellow')))
        if database.check_data(id_key=user) is None:
            break
        else:
            colors.color_print('[X] Esse usuário ja está em uso.', 'red')
    password = str(input(colors.color_string('Escolha uma senha: ', 'yellow')))
    database.add_data(data=f'{user}|{password}')


database = SqlEmu()
# Show options and guarantee a right response of the user
while True:
    colors.color_print('[1] Efetuar login\n[2] Cadastrar-se\n[3] Sair', 'yellow')
    # The user will get break if put a null response or a string
    while True:
        try:
            user_choice = int(input(colors.color_string('>>> ', 'yellow')))
        except ValueError:
            colors.color_print('[X] Resposta inválida!', 'red')
            continue
        break
    # The user will get break if the response not 1, 2 or 3
    while user_choice not in (1, 2, 3):
        colors.color_print('[X] Resposta inválida!', 'red')
        user_choice = int(input(colors.color_string('>>> ', 'yellow')))
    # If the response is 1 the user will enter on a login screen
    if user_choice == 1:
        while True:
            log_in = login()
            if not log_in:
                colors.color_print('[X] ACESSO NEGADO', 'red')
            else:
                break
        colors.color_print('[*] ACESSO PERMITIDO', 'green')
        break
    # If the response is 2 the user will enter on a register screen
    elif user_choice == 2:
        register()
    else:
        colors.color_print('Volte Sempre ^^', 'yellow')
        break
