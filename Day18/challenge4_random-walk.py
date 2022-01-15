# Generating a random walk in turtle.
from turtle import Turtle, Screen
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tim = Turtle()

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(400):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
