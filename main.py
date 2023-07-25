from turtle import Turtle
import turtle as t
import random

tim = Turtle()
t.colormode(255)
tim.hideturtle()

color_bank = [(2, 64, 87), (192, 161, 156), (141, 41, 43), (14, 122, 178), (185, 207, 192), (205, 161, 88), (6, 69, 48), (116, 41, 20), (36, 36, 36), (146, 38, 26), (108, 160, 174), (221, 161, 13), (151, 154, 87), (226, 179, 145), (78, 41, 49), (212, 191, 50), (159, 123, 51), (91, 142, 49), (5, 50, 83), (186, 99, 55), (182, 95, 78), (100, 70, 92), (115, 30, 27), (173, 195, 129), (60, 154, 142)]


x = -100
y = -100

for _ in range(6):
  tim.penup()
  tim.setpos(x, y)
  for _ in range(6):
    tim.dot(20, random.choice(color_bank))
    tim.forward(40)
  y += 40
