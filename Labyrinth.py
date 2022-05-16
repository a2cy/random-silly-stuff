import turtle


def update_screen():
    global player_position, player_health, found_walls
    turtle.clear()

    for i in range(10**2):
        turtle.penup()
        turtle.goto(i//10*30-30*5, i % 10*30-30*5)
        turtle.pendown()

        for j in range(4):
            turtle.fd(30)
            turtle.lt(90)

    for wall in found_walls:
        turtle.penup()
        turtle.goto(wall[0]*30-30*5, -wall[1]*30+30*4)
        turtle.pendown()

        turtle.fillcolor("black")
        turtle.begin_fill()

        for j in range(4):
            turtle.fd(30)
            turtle.lt(90)

        turtle.end_fill()

    turtle.penup()
    turtle.goto(player_position[0]*30-30*5+15, -player_position[1]*30+30*4+15)
    turtle.dot(15)

    turtle.goto(-100, 160)
    turtle.write(f'Verbleibende Leben: {player_health}', font=(
        "Verdana", 15, "normal"))

    turtle.goto(125, -145)
    turtle.write(f'Ziel', font=(
        "Verdana", 10, "normal"))

    turtle.update()


def click_regsitration(x, y):
    global game_field, player_position, player_health, found_walls
    new_player_position = [int(x//30+5), int((y//30-4)*-1)]

    move_allowed = (0 <= new_player_position[0] < 10 and 0 <= new_player_position[1] < 10 and
                    new_player_position[0] == player_position[0]+1 and new_player_position[1] == player_position[1] or
                    new_player_position[0] == player_position[0]-1 and new_player_position[1] == player_position[1] or
                    new_player_position[0] == player_position[0] and new_player_position[1] == player_position[1]+1 or
                    new_player_position[0] == player_position[0] and new_player_position[1] == player_position[1]-1)

    if move_allowed:
        if game_field[new_player_position[1]][new_player_position[0]] == 0:
            player_position = new_player_position

        else:
            player_health -= 1
            found_walls.append(new_player_position)

        update_screen()

        if player_position == [9, 9]:
            turtle.penup()
            turtle.goto(-50, 200)
            turtle.write(f'Gewonnen', font=(
                "Verdana", 15, "normal"))

            turtle.update()
            turtle.exitonclick()

        if player_health < 1:
            turtle.penup()
            turtle.goto(-40, 200)
            turtle.write(f'Verloren', font=(
                "Verdana", 15, "normal"))

            turtle.update()
            turtle.exitonclick()


game_field = [[0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 1, 1, 0, 1, 1, 0],
              [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
              [0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
              [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
              [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
              [1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
              [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
              [0, 1, 0, 0, 1, 0, 0, 0, 1, 0]]

player_position = [0, 0]
player_health = 300
found_walls = []

screen = turtle.Screen()
screen.onclick(click_regsitration)

turtle.tracer(0, 0)
turtle.hideturtle()

update_screen()

turtle.mainloop()
