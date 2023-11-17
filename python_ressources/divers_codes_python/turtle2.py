import turtle
turtle.color("red", "yellow")
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(90)
    if abs(pos()) < 1:
        pass
turtle.end_fill()
turtle.done()
