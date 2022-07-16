import sys
import math
import random
import turtle


class Throw:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Throw")
        
        turtle.tracer(0, 0)
        turtle.hideturtle()

        self.tower_height = random.randint(40, 200)
        self.tower_distance = random.randint(100, 500)
        self.try_count = 3

        self.start_y = 0
        self.angle = 0
        self.start_velocity = 0

        self.update_screen()

        turtle.update()

        self.run()

 
    def update_screen(self):
        turtle.clear()
        
        turtle.home()
        turtle.pendown()
        turtle.goto(self.tower_distance, 0)
        turtle.goto(self.tower_distance, self.tower_height)
        turtle.penup()

        turtle.goto(-55, 160)
        turtle.write(f"Trys left : {self.try_count}", font=(
            "Verdana", 15, "normal"))

        if not self.start_y or not self.angle or not self.start_velocity:
            return

        turtle.tracer(1, 6)
        turtle.home()
        turtle.pendown()

        x = 0
        while turtle.pos()[1] > -1:
            y = self.start_y + math.tan(math.radians(self.angle)) * x - 9.81 / (2 * self.start_velocity**2 * (math.cos(math.radians(self.angle))**2)) * x**2
            turtle.goto(x, y)

            if turtle.pos()[0] == self.tower_distance-1 and turtle.pos()[1] <= self.tower_height:
                turtle.penup()
                turtle.goto(-60, 200)
                turtle.write("You hit the wall!", font=(
                    "Verdana", 15, "normal"))

                return True

            x += 1

        turtle.tracer(0, 0)
        turtle.hideturtle()
        turtle.penup()

        turtle.goto(-70, 200)
        turtle.write("You didn't hit the wall.", font=(
            "Verdana", 15, "normal"))

        return False


    def run(self):
        while 1:
            try:
                if self.try_count > 0: 
                    self.start_y = turtle.numinput("Thow", "Enter launch height")
                    self.angle = turtle.numinput("Thow", "Enter launch angle")
                    self.start_velocity = turtle.numinput("Throw", "Enter launch velocity")

                    if not self.start_y and not self.angle and not self.start_velocity:
                        break
                    
                    self.try_count -= 1

                    hit = self.update_screen()

                    if hit:
                        self.try_count = 0

                    self.start_y = 0
                    self.angle = 0
                    self.start_velocity = 0

                turtle.update()

            except:
                break


if __name__ == "__main__":
    Throw()