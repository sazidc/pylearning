## Using turtle module to make a square

from turtle import Turtle, exitonclick

tim = Turtle()

tim.color("cadetblue")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# exitonclick()


# draw dashed lines 50 times

for _ in range(20):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

exitonclick()



