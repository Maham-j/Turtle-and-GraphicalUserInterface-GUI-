from turtle import Turtle, Screen
import random

timmy = Turtle()
'''random direction and bold '''
direction = [0, 90, 180, 270, 360]

def change_color():
    R = random.random()
    G = random.random()
    B = random.random()
    color = timmy.color(R, G, B)


for _ in range(100):
    timmy.width(10)
    timmy.speed('fastest')
    timmy.forward(20)
    timmy.setheading(random.choice(direction))
    change_color()



screen = Screen()
screen.exitonclick()

