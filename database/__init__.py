import colors
from random import randint


class SqlSim:
    def __init__(self):
        # Verify if the file exists or create them.
        try:
            colors.color_print('[*] Checking database...', 'grey')
            self.check_file()
        except FileNotFoundError:
            colors.color_print('[X] Database not found', 'red')
            colors.color_print('[*] Creating a new database...', 'grey')
            self.create_file()
        self.session = self.database_session()

    # Check file integrity.
    def check_file(self):
        with open('.db.txt', 'r') as file:
            file.close()

    # Create the file.
    def create_file(self):
        with open('.db.txt', 'w') as file:
            file.close()

    # Extract data from .db.txt and create a 'session' as list
    def database_session(self):
        users_list = []
        with open('.db.txt', 'r') as database:
            db = database.readlines()
        # Encapsulates all user data into a dictionary before putting it on the list
        for data in db:
            temp = {}
            # Slice the data with an separator
            sliced_data = data.split(sep=';')
            id = sliced_data[0]
            user = sliced_data[1]
            password = sliced_data[2]
            temp['-id-'] = id
            temp['-usr-'] = user
            temp['-psw-'] = password
            users_list.append(temp)
        # Return a list of users
        return users_list

    def database_save(self):
        # Put all the session data inside the .db.txt again.
        with open('.db.txt', 'w') as file:
            for person in self.session:
                file.write(f'{person["-id-"]};{person["-usr-"]};{person["-psw-"]};\n')

    def add_data(self, user, password):
        # Add a new user to the database with an random ID
        id = self.id_creator()
        self.session.append({'-id-': id, '-usr-': user, '-psw-': password})

    def id_creator(self):
        # Create an random ID of 5 digits
        id = randint(10000, 99999)
        return id

    def check_data(self, user, password):
        for person in self.session:
            # If the user is correct:
            if person['-usr-'] == user:
                # If the password is also correct:
                if person['-psw-'] == password:
                    return person['-id-'] # return the ID if user is into the database and the password MATCHES
                return 0 # return 0 if the user is into the database but the password is INCORRECT
        return 1 # Return 1 if the loop ends and the user is NOT FOUND
