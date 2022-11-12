empty_cell = '-'


def print_game_field(game_field):
    '''Отображает игровое поле в консоли'''
    print()
    for row in game_field:
        print(" ".join(row))
    print()


def get_cell_coords(current_mark):
    '''Запрашивает координаты ячейки для ввода.'''
    cell_coords = None

    try:
        cell_coords = list(map(int, input(f'Координаты ячейки для "{current_mark}": ').split()))

        if len(cell_coords) != 2:
            cell_coords = None
            raise Exception('Необходимо указать две координаты')

        elif cell_coords[0] < 1 or cell_coords[0] > 3:
            cell_coords = None
            raise Exception('Номер строки должен быть в диапазоне от 1 до 3 включительно')

        elif cell_coords[1] < 1 or cell_coords[1] > 3:
            cell_coords = None
            raise Exception('Номер столбца должен быть в диапазоне от 1 до 3 включительно')

    except ValueError:
        print('Координаты ячейки должны быть числом')

    except Exception as e:
        print(e)

    finally:
        return cell_coords


def update_game_field(*args):
    '''Обновляет игровое поле'''
    mark, cell_coords, game_field = args
    x = cell_coords[0]
    y = cell_coords[1]
    
    if game_field[x][y] != empty_cell:
        print('Ячейка занята')
        return False
    else:
        game_field[x][y] = mark
        return True


def analyze_game_field(game_field):
    '''Анализирует игровое поле на наличие победителя'''
    if game_field[1][1] != empty_cell and game_field[1][1] == game_field[1][2] == game_field[1][3]:
        return True
    elif game_field[2][1] != empty_cell and game_field[2][1] == game_field[2][2] == game_field[2][3]:
        return True
    elif game_field[3][1] != empty_cell and game_field[3][1] == game_field[3][2] == game_field[3][3]:
        return True
    elif game_field[1][1] != empty_cell and game_field[1][1] == game_field[2][1] == game_field[3][1]:
        return True
    elif game_field[1][2] != empty_cell and game_field[1][2] == game_field[2][2] == game_field[3][2]:
        return True
    elif game_field[1][3] != empty_cell and game_field[1][3] == game_field[2][3] == game_field[3][3]:
        return True
    elif game_field[1][1] != empty_cell and game_field[1][1] == game_field[2][2] == game_field[3][3]:
        return True
    elif game_field[3][1] != empty_cell and game_field[3][1] == game_field[2][2] == game_field[1][3]:
        return True
    else:
        return False


def start_game():
    '''Начинает игру'''
    game_field = [
        [' ', '1', '2', '3'],
        ['1', empty_cell, empty_cell, empty_cell],
        ['2', empty_cell, empty_cell, empty_cell],
        ['3', empty_cell, empty_cell, empty_cell]
    ]

    print('-' * 80)
    print('Добро пожаловать в игру "Крестики-нолики"!')
    print()
    print('Правила игры:')
    print('* первым ходит игрок, который ставит "x";')
    print('* для выбора ячейки введите два числа через пробел, например, "1 2",')
    print('* где 1 - номер строки, 2 - номер столбца.')
    print('-' * 80)
    print_game_field(game_field)

    x_mark = 'x'
    o_mark = 'o'
    current_mark = x_mark
    current_step = 1
    total_steps = 12

    while True:
        if current_step == total_steps:
            print('Ничья. Игра окончена.')
            break
        else:
            cell_coords = get_cell_coords(current_mark)

            if cell_coords:
                updated = update_game_field(current_mark, cell_coords, game_field)

                if updated:
                    print_game_field(game_field)

                    won = analyze_game_field(game_field)

                    if won:
                        print('Вы выиграли!')
                        break
                    else:
                        if current_mark == x_mark:
                            current_mark = o_mark
                        else:
                            current_mark = x_mark
                        current_step += 1


if __name__ == '__main__':
    start_game()
