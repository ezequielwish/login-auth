from msilib.schema import TextStyle
from types import FrameType
from database import SqlSim
import PySimpleGUI as sg


class Auth:
    def __init__(self):
        # Window Layout
        sg.theme('Material1')
        self.layout = [
            [sg.Frame(title='Insira seus dados', title_location=sg.TITLE_LOCATION_TOP , 
            layout=[
                [sg.Text('Usuário:', size=(7, 0)), sg.Input(size=(15, 0), key='-usr-')], 
                [sg.Text('Senha:', size=(7, 0)), sg.Input(size=(15, 0), key='-pwd-', password_char='*')]
            ])],
            [sg.Button('Fazer login', key='login', bind_return_key=True), sg.Button('Cadastrar-se', key='register')]
        ]
        # Create a window
        self.window = sg.Window('Login', layout=self.layout)
        self.sql = SqlSim()

    def run(self):
            try:
                while True:
                    button, values = self.window.Read()
                    if button == sg.WIN_CLOSED:
                        break
                    user = values['-usr-']
                    password = values['-pwd-']
                    # If user click on the Login button
                    if button == 'login':
                        self.login(user, password)
                    # If user click on the Register button
                    elif button == 'register':
                        self.register(user, password)
            finally:
                # Save changes in database
                self.sql.database_save()

    def login(self, user, password):
        # Check if user exist
        search = self.sql.check_data(user, password)
        # If return 0 the user exists but the password doesn't match
        if search == 0:
            sg.popup('Senha incorreta!')
        # If return 1 the user is not registered
        elif search == 1:
            sg.popup('Usuário inexistente!')
        # Return the user ID if the user and the password matches in the database
        else:
            sg.popup(f'Sucesso!\nID do usuário: {search}')
            # You can use the user ID to open a PERSONAL window for this user
            # Change to window.hide() if you want to open another window after the authentification
            self.window.close()

    # Register a new user
    def register(self, user, password):
        # Check if the user already in use, if return 1, the user is not in use
        if self.sql.check_data(user, password) == 1:
            self.sql.add_data(user, password)
            print('User registered')
        # If return 0 or an user ID, the user is already in use
        else:
            print('User already in use!')


login_window = Auth()
login_window.run()
