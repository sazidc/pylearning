# Using turtle module to make a square

from turtle import Turtle

tim = Turtle()

tim.color("coral")
for _ in range(4):
    tim.forward(100)
    tim.right(90)

tim.exitonclick()
