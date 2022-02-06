from database import SqlEmu
import colors

db = SqlEmu()
user = 'ezequiel'
passw = '123'
in_database = db.check_data(id_key=user, data=passw, sep=';')
if in_database is None:
    db.add_data(f'{user};{passw}')
else:
    colors.color_print('[*] User already in use', 'red')
