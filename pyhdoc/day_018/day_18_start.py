## Using turtle module to make a square

from turtle import Turtle, exitonclick

tim = Turtle()

tim.color("cadetblue")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# exitonclick()


# # draw dashed lines 50 times

# for _ in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# exitonclick()

# # draw different shapes like triangle, square, pentagon, hexagon, etc

for _ in range(3):
    tim.forward(100)
    tim.right(120)

tim.color("red")

for _ in range(4):
    tim.forward(100)
    tim.right(90)

tim.color("green")

for _ in range(5):
    tim.forward(100)
    tim.right(72)

tim.color("blue")

for _ in range(6):
    tim.forward(100)
    tim.right(60)

tim.color("brown")

for _ in range(7):
    tim.forward(100)
    tim.right(51.43)

tim.color("orange")

for _ in range(8):
    tim.forward(100)
    tim.right(45)

tim.color("violet")

for _ in range(9):
    tim.forward(100)
    tim.right(40)

tim.color("black")

for _ in range(10):
    tim.forward(100)
    tim.right(36)

exitonclick()

