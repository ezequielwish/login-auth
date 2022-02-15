from database import SqlEmu
import PySimpleGUI as Gui


class Login:
    def __init__(self):
        self.layout = [
            [Gui.Text('Usuário:', size=(7, 0)), Gui.Input(size=(15, 0), key='user')],
            [Gui.Text('Senha:', size=(7, 0)), Gui.Input(size=(15, 0), key='password')],
            [Gui.Button('Fazer Login', key='login'), Gui.Button('Cadastrar-se', key='join')]
        ]
        self.window = Gui.Window('Login', layout=self.layout)

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
