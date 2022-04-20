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
        self.sql = SqlEmu()

    def init(self):
            try:
                while True:
                    button, values = self.window.Read()
                    if button == Gui.WIN_CLOSED:
                        break
                    user = values['user']
                    password = values['password']
                    if button == 'login':
                        pass
                    elif button == 'join':
                        self.sql.add_data(user=user, password=password)
            finally:
                self.sql.database_update()


window = Login()
window.init()
