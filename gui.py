from database import SqlEmu
import PySimpleGUI as gui

class Login:
    def __init__(self):
        self.layout = [
            [gui.Text('Usuário:', size=(7,0)), gui.Input(size=(15,0), key='user')],
            [gui.Text('Senha:', size=(7,0)), gui.Input(size=(15,0), key='password')],
            [gui.Button('Fazer Login', key='login'), gui.Button('Cadastrar-se', key='join')]
        ]
        self.window = gui.Window('Login', layout=self.layout)

    def init(self):
        while True:
            button, values = self.window.Read()
            user = values['user']
            password = values['password']
            if button == 'login':
                print(f'({user}|{password}) logado.')
            elif button == 'join':
                print(f'({user}|{password}) cadastrado.')


screen = Login()
screen.init()
