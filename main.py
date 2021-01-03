from turtle import Turtle, Screen
import random
my_turtle = Turtle()
my_turtle.shape("arrow")

def change_color():
    R = random.random()
    G = random.random()
    B = random.random()
    my_turtle.color(R, G, B)
n = 3
for _ in range(7):
    change_color()

    for _ in range(n):
        my_turtle.forward(100)
        my_turtle.right(360/n)
    n += 1


screen=Screen()
screen.exitonclick()











