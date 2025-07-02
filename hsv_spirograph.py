import turtle
import colorsys

screen = turtle.Screen()
screen.title("HSV Spirograph")

pen = turtle.Turtle()
pen.speed(0)
turtle.bgcolor("black")

hue = 0
for i in range(120):
    pen.color(colorsys.hsv_to_rgb(hue, 1, 1))
    pen.circle(150)
    pen.left(3)
    hue += 0.008333

turtle.done()