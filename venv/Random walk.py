from turtle import Turtle, Screen
import random
my_turtle = Turtle()
my_turtle.shape("turtle")
def change_color():
    R = random.random()
    G = random.random()
    B = random.random()
    my_turtle.color(R, G, B)
direction = [0, 90, 180, 270]
my_turtle.speed("fast")
my_turtle.pensize(15)
for _ in range(200):
    my_turtle.forward(30)
    my_turtle.setheading(random.choice(direction))
    change_color()


screen=Screen()
screen.exitonclick()