def win_and_pooh(song):
    volwes = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
    parts = song.split()
    lst = list()
    for item in parts:
        k = 0
        for letter in item:
            if letter in volwes:
                k += 1
        lst.append(k)
    if len(set(lst)) == 1:
        print('Парам пам-пам')
    else:
        print('Пам парам')


########################################################################################################################

def print_operation_table(operation, num_rows=6, num_columns=6):
    a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in a:
        print(*[f"{x:>3}" for x in i])

print_operation_table(lambda x, y: x * y)
