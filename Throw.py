import math
import random
import turtle

def wurfParabel(yo, a, vo, turm_w, turm_h):
    x = 0
    while turtle.pos()[1] > -1:
        y = yo + math.tan(math.radians(a)) * x - 9.81 / (2 * vo**2 * (math.cos(math.radians(a))**2)) * x**2
        turtle.goto(x, y)

        if turtle.pos()[0] == turm_w-1 and turtle.pos()[1] <= turm_h:
            return "You hit the wall!"

        x += 1
        
    return "You didn't hit the wall."

turtle.shape("circle")
turtle.shapesize(.2)

turm_h = random.randint(40, 200)
turm_w = random.randint(100, 500)
    
turtle.goto(1000, 0)
turtle.goto(turm_w, 0)
turtle.goto(turm_w, turm_h)
turtle.goto(turm_w, 0)
turtle.home()

for i in range(1,4):
    print(f"Try : {i}")
        
    yo = float(input("Enter launch height : "))
    a = float(input("Enter launch angle : "))
    vo = float(input("Enter launch speed : "))

    wurf_treffer = wurfParabel(yo=yo, a=a, vo=vo, turm_w=turm_w, turm_h=turm_h)
    print(wurf_treffer)

    if wurf_treffer == "You hit the wall!":
        break
        
    turtle.penup()
    turtle.home()
    turtle.pendown()

turtle.mainloop()