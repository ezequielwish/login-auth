import colors


class SqlEmu:
    def __init__(self):
        self._file = 'users.txt'
        # Verify if the file exists or create them.
        try:
            colors.color_print('[*] Checking database...', 'grey')
            self.check_file()
        except FileNotFoundError:
            colors.color_print('[*] Database not found! Lets create!', 'red')
            colors.color_print('[*] Creating a new database...', 'grey')
            self.create_file()

    # Check file integrity.
    def check_file(self):
        with open(self._file, 'r') as file:
            file.close()

    # Create the file.
    def create_file(self):
        with open(self._file, 'w') as file:
            file.close()

    # Split the data of a list and put on a dictionary with the first item as ID
    @staticmethod
    def list_to_dict(data_as_list, sep):
        data_as_dict = {}
        for data in data_as_list:
            key = data.split(sep=sep)[0]
            value = data.split(sep=sep)[1][:-1]
            data_as_dict[key] = value
        return data_as_dict

    def check_data(self, id_key, data, sep=None):
        """
        Checks if a data is in the database
        :param id_key: ID of the data (first param before the separator)
        :param data: Rest of the content
        :param sep: Data separator
        :return: True: if the ID was founded,
                 False: if the ID was founded but the data does not correspond
                 None: if the ID was not founded
        """
        with open(self._file, 'r') as database:
            data_as_list = database.readlines()
            data_as_dict = self.list_to_dict(data_as_list, sep=sep)
            for key, value in data_as_dict.items():
                if id_key == key:
                    if data == value:
                        return True
                    else:
                        return False
            return None

    # Clean the database and rebuild with new information
    def database_update(self, data_as_list):
        with open(self._file, 'w') as file:
            file.writelines(data_as_list)
        colors.color_print('[*] Database updated.', 'grey')

    # Add anything to the database
    def add_data(self, data):
        with open(self._file, 'r') as database:
            data_as_list = database.readlines()
            data_as_list.append(data+'\n')
        self.database_update(data_as_list)

