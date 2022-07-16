import turtle


class Labyrinth():
    
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Labyrith")
        self.screen.onclick(self.click_registration)

        turtle.tracer(0, 0)
        turtle.hideturtle()

        self.game_grid = [[0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                         [0, 0, 0, 1, 1, 1, 0, 1, 1, 0],
                         [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                         [0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
                         [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
                         [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
                         [1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
                         [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
                         [0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
                         [0, 1, 0, 0, 1, 0, 0, 0, 1, 0]]

        self.player_position = [0, 0]
        self.player_health = 3
        self.found_walls = []

        self.update_screen()

        self.run()


    def update_screen(self):
        turtle.clear()

        for i in range(10**2):
            turtle.penup()
            turtle.goto(i//10*30-30*5, i % 10*30-30*5)
            turtle.pendown()

            for j in range(4):
                turtle.fd(30)
                turtle.lt(90)

        for wall in self.found_walls:
            turtle.penup()
            turtle.goto(wall[0]*30-30*5, -wall[1]*30+30*4)
            turtle.pendown()

            turtle.fillcolor("black")
            turtle.begin_fill()

            for i in range(4):
                turtle.fd(30)
                turtle.lt(90)

            turtle.end_fill()

        turtle.penup()
        turtle.goto(self.player_position[0]*30-30*5+15, -self.player_position[1]*30+30*4+15)
        turtle.dot(15)

        turtle.goto(-100, 160)
        turtle.write(f"Remaining lives : {self.player_health}", font=(
            "Verdana", 15, "normal"))

        turtle.goto(125, -145)
        turtle.write(f"End", font=(
            "Verdana", 10, "normal"))


    def click_registration(self, x, y):
        new_player_position = [int(x//30+5), int((y//30-4)*-1)]

        move_allowed = (0 <= new_player_position[0] < 10 and 0 <= new_player_position[1] < 10 and
                        (new_player_position[0] == self.player_position[0]+1 and new_player_position[1] == self.player_position[1] or
                        new_player_position[0] == self.player_position[0]-1 and new_player_position[1] == self.player_position[1] or
                        new_player_position[0] == self.player_position[0] and new_player_position[1] == self.player_position[1]+1 or
                        new_player_position[0] == self.player_position[0] and new_player_position[1] == self.player_position[1]-1))

        if move_allowed:
            if self.game_grid[new_player_position[1]][new_player_position[0]] == 0:
                self.player_position = new_player_position

            else:
                self.player_health -= 1
                self.found_walls.append(new_player_position)

            self.update_screen()

            if self.player_position == [9, 9]:
                turtle.penup()
                turtle.goto(-50, 200)
                turtle.write(f"You won!", font=(
                    "Verdana", 15, "normal"))

                self.screen.onclick(None)

            if self.player_health < 1:
                turtle.penup()
                turtle.goto(-40, 200)
                turtle.write(f"You lost.", font=(
                    "Verdana", 15, "normal"))

                self.screen.onclick(None)


    def run(self):
        while 1:
            try:
                turtle.update()
            except:
                break


if __name__ == "__main__":
    Labyrinth()
