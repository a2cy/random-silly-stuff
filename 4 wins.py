import random


def find_highest_spot(x):
    for y, i in enumerate(play_field):
        if not i[x] == "_":
            return y-1

        if y == 5:
            return y


def print_play_field():
    for i in range(40):
        print("")

    print(f"Current player : {current_player}")

    for line in play_field:
        print(
            f"{line[0]}  {line[1]}  {line[2]}  {line[3]}  {line[4]}  {line[5]}  {line[6]}")
    
    print("1  2  3  4  5  6  7")


def check_win():
    # horizontal
    for i in play_field:
        x_count = 0
        for j in i:
            if j == player1:
                x_count += 1
            else:
                x_count = 0

            if x_count == 4:
                x_count = 0
                return player1

    for i in play_field:
        y_count = 0
        for j in i:
            if j == player2:
                y_count += 1
            else:
                y_count = 0

            if y_count == 4:
                y_count = 0
                return player2

    # vertical
    for j in range(7):
        x_count = 0
        for i in range(6):
            if play_field[i][j] == player1:
                x_count += 1
            else:
                x_count = 0

            if x_count == 4:
                x_count = 0
                return player1

    for j in range(7):
        y_count = 0
        for i in range(6):
            if play_field[i][j] == player2:
                y_count += 1
            else:
                y_count = 0

            if y_count == 4:
                y_count = 0
                return player2
    
    temp_list = []
    for line in play_field:
        temp_list.extend(line)

    if not "_" in temp_list:
        return ""


play_field = [["_", "_", "_", "_", "_", "_", "_"],
              ["_", "_", "_", "_", "_", "_", "_"],
              ["_", "_", "_", "_", "_", "_", "_"],
              ["_", "_", "_", "_", "_", "_", "_"],
              ["_", "_", "_", "_", "_", "_", "_"],
              ["_", "_", "_", "_", "_", "_", "_"]]

allowed_inputs = {"1", "2", "3", "4", "5", "6", "7"}

player1, player2 = "X", "O"

current_player = random.choice((player1, player2))

while 1:
    print_play_field()

    winner = check_win()
    if winner:
        print(f"Player {winner} won.")
        break

    new_column = input("Enter new column : ")

    if new_column in allowed_inputs:
        new_column = int(new_column) - 1
    else:
        continue

    if play_field[find_highest_spot(new_column)][new_column] == "_":
        play_field[find_highest_spot(new_column)][new_column] = current_player

        if current_player == player1:
            current_player = player2
        else:
            current_player = player1
