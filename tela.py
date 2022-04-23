import PySimpleGUI as sg

def window():
    layout = [
        [sg.Frame('titulo', layout=[[sg.Text('Contato 1:')]])],
        [],
        [],
    ]
    return sg.Window('testando', layout=layout)

while True:
    button, value = window().read()
    if button == sg.WIN_CLOSED:
        break
