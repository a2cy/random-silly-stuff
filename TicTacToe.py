import random


def print_play_field():
    for i in range(40):
        print('')

    print(f'Nächster Zug : {current_player}')

    for line in play_field:
        print(f'{line[0]} {line[1]} {line[2]}')


def check_win():
    # horizontal
    for i in range(3):
        if play_field[i][0] == play_field[i][1] == play_field[i][2]:
            if play_field[i][0] != '_':
                return play_field[i][0]
   
    # vertical
    for i in range(3):
       if play_field[0][i] == play_field[1][i] == play_field[2][i]:
            if play_field[0][i] != '_':
                return play_field[0][i]
    
    # diagonal1
    if play_field[0][0] == play_field[1][1] == play_field[2][2]:
        if play_field[0][0] != '_':
            return play_field[0][0]
    
    # diagonal2
    if play_field[0][2] == play_field[1][1] == play_field[2][0]:
        if play_field[0][2] != '_':
            return play_field[0][2]
    
    temp_list = []
    for line in play_field:
        temp_list.extend(line)

    if not '_' in temp_list:
        return 'Unentschieden'


play_field = [['_', '_', '_'],
              ['_', '_', '_'],
              ['_', '_', '_']]

allowed_entrys = {'1', '2', '3'}
player1, player2 = 'X', 'O'
current_player = random.choice((player1, player2))

while 1:
    print_play_field()

    winner = check_win()
    if winner:
        print(f'Der Gewinner des Spiels ist : {winner}')
        break

    new_line = input('Gebe die Zeile des neuen Eintrags ein : ')
    new_column = input('Gebe die Spalte des neuen Eintrags ein : ')

    if new_line in allowed_entrys and new_column in allowed_entrys:
        new_line = int(new_line) - 1
        new_column = int(new_column) - 1
    else:
        continue

    if play_field[new_line][new_column] == '_':
        play_field[new_line][new_column] = current_player

        if current_player == player1:
            current_player = player2
        else:
            current_player = player1
