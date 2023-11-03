import turtle
import random
import time

# 添加背景和爪子
def add():
    turtle.bgpic('bg.gif')
    image = 'claw.gif'
    turtle.addshape(image)
    turtle.shape(image)
    turtle.penup()
    turtle.goto(0, 300)

add()
def fun_null(x, y):
    return
def grab(x, y):
    turtle.onscreenclick(fun_null)
    # 爪子来回移动
    i = 1
    while i <= 3:
        turtle.goto(200, 300)
        turtle.goto(-200, 300)
        i = i + 1
    x = random.randint(-200, 200)
    turtle.goto(x, 300)
    # 抓娃娃奖品
    time.sleep(0.3)
    turtle.goto(x, 50)
    time.sleep(0.5)
    # 创新1
    image = 'claw2.gif'
    turtle.addshape(image)
    turtle.shape(image)
    turtle.goto(x, 300)
    time.sleep(0.5)

    turtle.hideturtle()
    # 随机显示奖品
    turtle.bgpic('bg2.gif')
    turtle.goto(-40, -70)
    n = random.randint(1, 5)
    if n == 1:
        turtle.write('红烧肉', font=('arial', 30, 'bold'))
    elif n == 2:
        turtle.write('香辣虾', font=('arial', 30, 'bold'))
    elif n == 3:
        turtle.write('水煮鱼', font=('arial', 30, 'bold'))
    elif n == 4:
        turtle.write('炒牛肉', font=('arial', 30, 'bold'))
    else:
        turtle.write('三杯鸡', font=('arial', 30, 'bold'))
    # turtle.stamp()

turtle.onscreenclick(grab)
turtle.done()
