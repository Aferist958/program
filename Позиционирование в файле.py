a = {}
def custom_write(file_name, strings):
    file = open(file_name, 'w')
    for i in range(len(strings)):
        a[i + 1, file.tell()] = strings[i]
        file.write(strings[i] + '\n')
    return a



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)

print(result)
