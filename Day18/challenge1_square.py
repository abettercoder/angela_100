from turtle import Turtle, Screen

tim_the_turtle = Turtle()

for _ in range(4):
    tim_the_turtle.forward(100)
    tim_the_turtle.right(90)

screen = Screen()
screen.exitonclick()
