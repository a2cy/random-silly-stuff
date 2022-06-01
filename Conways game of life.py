import time
import turtle


class ConwaysGameOfLife():

    def __init__(self):
        self.game_grid = [[0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                         [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                         [1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        turtle.tracer(0, 0)
        turtle.hideturtle()

        self.update()


    def update_screen(self):
        turtle.clear()

        for i in range(10**2):
            turtle.penup()
            turtle.goto(i//10*30-30*5, i % 10*30-30*5)
            turtle.pendown()

            for j in range(4):
                turtle.fd(30)
                turtle.lt(90)

        turtle.penup()
        for i in range(10**2):
            x = i % 10
            y = i//10

            if self.game_grid[9-y][x] == 1:
                turtle.goto(x*30-30*4.5, y*30-30*4.5)
                turtle.dot(15)


    def count_neighbours(self, _x, _y, game_grid):
        count = 0
        for i in range(3**2):
            x = _x+i % 3-1
            y = _y+i//3-1
            if 0<=x<=9 and 0<=y<=9 and (x,y)!=(_x,_y):
                count += game_grid[y][x]

        return count


    def update_grid(self):
        new_game_grid = [[self.game_grid[y][x] for x in range(10)] for y in range(10)]
        for y in range(10):
            for x in range(10):
                neighbours = self.count_neighbours(x, y, self.game_grid)
                if neighbours < 2:
                    new_game_grid[y][x] = 0

                elif neighbours == 3:
                    new_game_grid[y][x] = 1

                elif neighbours > 3:
                    new_game_grid[y][x] = 0
    
        self.game_grid = new_game_grid
    

    def update(self):
        while 1:
            self.update_grid()
            self.update_screen()
            turtle.update()
            time.sleep(.4)


if __name__ == '__main__':
    game = ConwaysGameOfLife()
