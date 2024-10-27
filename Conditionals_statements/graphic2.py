from turtle import *
import colorsys as p

title("niTin KM")
bgcolor("black")
tracer(100)
h = 0.1

for i in range(2000):
    c = p.hsv_to_rgb(h, 1, 1)
    fillcolor(c)
    h += 0.003
    begin_fill()
    circle(170, 72)
    left(91)
    left(20)
    circle(170, 20)
    right(18)
    end_fill()

done()
