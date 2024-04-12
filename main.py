gomoku = [i for i in range(1,10)] #игровое поле
gomoku_step = 3
#рисую игровое поле
def print_gomoku():
    print(('_' * 4 * gomoku_step))
    for i in range(gomoku_step):
        print((' '*gomoku_step + '|') * 2)
        print(gomoku[i * gomoku_step], ' |', gomoku[1 + i*gomoku_step], '|', gomoku[2 + i*gomoku_step])
        print(('_' * 4)*gomoku_step)

#ход игрока
def step(index, char):
    if index > 9  or index < 1 or gomoku[index - 1] in ('X', 'O'):
        return False
    gomoku[index - 1] = char
    return True
    pass

def if_win(gomoku):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if gomoku[each[0]] == gomoku[each[1]] == gomoku[each[2]]:
            return gomoku[each[0]]
    return False

def start():
    now_playing = 'X' #текущий игрок
    turn = 1 #номер хода
    print_gomoku()
    while (turn < 10) and (if_win(gomoku) == False):
        index = int(input('Ходит игрок ' + now_playing + '\nВведите номер игрового поля (0 -выход):'))
        if index == 0:
            break
        if step(index, now_playing):
            print('Ход совершён')
            if (now_playing == 'X'):
                now_playing = 'O'
            else:
                now_playing = 'X'

        print_gomoku()
        turn += 1
    else:
        print('Неверное поле. Повторите ход')

    if turn == 10:
        print('Ничья')
    else:
        print('Выиграл' + if_win(gomoku))




print('Добро пожаловать, мой юный дуг! Хочешь поиграть?')
start()




