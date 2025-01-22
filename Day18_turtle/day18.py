# Turtle
# 20 Januari 2025

import turtle

window = turtle.Screen()
window.title("Belajar Turtle di Python")

pen = turtle.Turtle()
pen.color("blue")
pen.circle(50)

pen.penup()
pen.goto(-100, -100)
pen.pendown()

pen.color("red")
pen.circle(50)

pen.penup()
pen.goto(-200, -200)
pen.pendown()

pen.color("green")
pen.circle(50)


# for _ in range(100):
#     pen.forward(100)
#     pen.left(3)
#     pen.back(100)
#
turtle.done()