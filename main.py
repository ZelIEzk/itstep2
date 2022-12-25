def read_file(path):
    with open(path, 'r') as file:
        result = file.readlines()
        if not result:
            raise ValueError('Файл пуст!')

        return result


file_path = input('Введите путь к файлу:')

try:
    file_content = read_file(file_path)
except PermissionError as error:
    print('Что-то пошло не так:', error)

try:
    for line in file_content:
        print(line.strip('\n'))
except NameError as error:
    print('Что-то пошло не так:', error)