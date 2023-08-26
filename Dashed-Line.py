from turtle import Turtle, Screen
import random

timmy = Turtle()
''' for the dashed line'''
for _ in range(15):
    timmy.forward(10)
    timmy.color('white')
    timmy.forward(10)
    timmy.color('black')

screen = Screen()
screen.exitonclick()

  
