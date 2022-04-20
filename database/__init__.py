import colors


class SqlEmu:
    def __init__(self):
        # Verify if the file exists or create them.
        try:
            colors.color_print('[*] Checking database...', 'grey')
            self.check_file()
        except FileNotFoundError:
            colors.color_print('[X] Database not found', 'red')
            colors.color_print('[*] Creating a new database...', 'grey')
            self.create_file()
        self.handler = self.database_handler()

    # Check file integrity.
    def check_file(self):
        with open('users.txt', 'r') as file:
            file.close()

    # Create the file.
    def create_file(self):
        with open('users.txt', 'w') as file:
            file.close()

    def database_handler(self):
        db = []
        persons = []
        with open('users.txt', 'r') as database:
            db = database.readlines()
        for data in db:
            temp = {}
            user = data.split(sep=';')[0]
            password = data.split(sep=';')[1][:-1]
            temp['-usr-'] = user
            temp['-psw-'] = password
            persons.append(temp)
        return persons

    def database_update(self):
        temp = self.handler.copy()
        with open('users.txt', 'w') as file:
            for person in temp:
                file.write(f'{person["-usr-"]};{person["-psw-"]}\n')

    def add_data(self, user, password):
        self.handler.append({'-usr-': user, '-psw-': password})

    