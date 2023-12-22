#from turtle import *

turtle.color('red', 'yellow')
begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
