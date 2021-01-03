from turtle import Turtle, Screen
import random
my_turtle = Turtle()
my_turtle.shape("arrow")
def change_color():
    R = random.random()
    G = random.random()
    B = random.random()
    my_turtle.color(R, G, B)
my_turtle.speed("fastest")
for i in range(0,360,10):
    my_turtle.circle(100)
    my_turtle.setheading(i)
    change_color()



screen=Screen()
screen.exitonclick()