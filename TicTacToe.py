import random
import turtle


class TicTacToe:

    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("TicTacToe")
        self.screen.onclick(self.click_registration)

        turtle.hideturtle()
        turtle.tracer(0,0)

        self.game_grid = [["_","_","_"],
                          ["_","_","_"],
                          ["_","_","_"]]

        self.player_1, self.player_2 = "X", "O"
        self.current_player = random.choice([self.player_1, self.player_2])

        self.update_screen()

        turtle.update()

        self.run()


    def update_screen(self):
        turtle.clear()

        for i in range(3**2):
            turtle.penup()
            turtle.goto(i//3*30-30*1.5, i % 3*30-30*1.5)
            turtle.pendown()

            for i in range(4):
                turtle.fd(30)
                turtle.lt(90)
        
        turtle.penup()
        for i in range(3**2):
            x = i % 3
            y = i//3

            if self.game_grid[2-y][x] != "_":
                turtle.goto(x*30-30*1.2, y*30-30*1.4)
                turtle.write(self.game_grid[2-y][x], font=(
                    "Verdana", 15, "normal"))
        
        turtle.goto(-80, 50)
        turtle.write(f"Current player: {self.current_player}", font=(
                "Verdana", 15, "normal"))
        
        turtle.update()


    def check_win(self):
        # horizontal
        for i in range(3):
            if self.game_grid[i][0] == self.game_grid[i][1] == self.game_grid[i][2]:
                if self.game_grid[i][0] != "_":
                    return self.game_grid[i][0]
   
        # vertical
        for i in range(3):
           if self.game_grid[0][i] == self.game_grid[1][i] == self.game_grid[2][i]:
                if self.game_grid[0][i] != "_":
                    return self.game_grid[0][i]
    
        # diagonal1
        if self.game_grid[0][0] == self.game_grid[1][1] == self.game_grid[2][2]:
            if self.game_grid[0][0] != "_":
                return self.game_grid[0][0]
    
        # diagonal2
        if self.game_grid[0][2] == self.game_grid[1][1] == self.game_grid[2][0]:
            if self.game_grid[0][2] != "_":
                return self.game_grid[0][2]
    
        temp_list = []

        for line in self.game_grid:
            temp_list.extend(line)

        if not "_" in temp_list:
            return ""


    def click_registration(self, x, y):
        x = int((x+30*1.5)//30)
        y = int(((y-30*.5)//30)*-1)

        move_allowed = (0 <= x < 3 and 0 <= y < 3 and self.game_grid[y][x] == "_")

        if move_allowed:
            self.game_grid[y][x] = self.current_player

            self.current_player = self.player_1 if self.current_player == self.player_2 else self.player_2

            self.update_screen()

        winner = self.check_win()

        if winner:
            turtle.penup()
            turtle.goto(-60, 70)
            turtle.write(f"Player {winner} won.", font=(
                "Verdana", 15, "normal"))

            self.screen.onclick(None)


    def run(self):
        while 1:
            try:
                turtle.update()
            except:
                break


if __name__ == "__main__":
    TicTacToe()