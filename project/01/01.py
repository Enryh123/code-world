import turtle
turtle.bgpic('man.gif')
image = 'hair.gif'
turtle.addshape(image)
turtle.shape(image)

def draw(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.stamp()

turtle.onscreenclick(draw)
turtle.hideturtle()
turtle.done()





