def colors_database():
    return{
            'dark': 0,
            'red': 1,
            'green': 2,
            'yellow': 3,
            'blue': 4,
            'magenta': 5,
            'cyan': 6,
            'grey': 7,
            'white': 8
            }


def color_print(text: str, color: str):
    print(f'\033[3{colors_database()[color]}m{text}\033[m')


def color_string(text: str, color: str):
    return f'\033[3{colors_database()[color]}m{text}\033[m'

