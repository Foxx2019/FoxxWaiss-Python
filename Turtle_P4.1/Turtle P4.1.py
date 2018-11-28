import turtle as t

def rosette():
    t.speed(0)
    t.bgcolor('black')
    circle1()
    circle2()
    circle3()
    t.exitonclick()


def circle1():
    t.pencolor('red')
    for x in range(90):
        t.circle(50)
        t.left(4)

def circle2():
    t.pencolor('magenta')
    for x in range(90):
        t.circle(100)
        t.left(4)

def circle3():
    t.pencolor('blue')
    for x in range(90):
        t.circle(150)
        t.left(4)



rosette()
