# import another module
# print (another_module.another_variable)
#
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("CadetBlue")
timmy.forward(100)
timmy.back(100)
timmy.forward(100)
timmy.back(100)


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
