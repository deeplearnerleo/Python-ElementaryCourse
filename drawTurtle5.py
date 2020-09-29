import turtle as t
t.setup(500,500,100,100)
t.penup()
t.pendown()
t.pensize(2)
t.pencolor("black")
'''
#t.turtle
t.goto(100,0)
for i in range(100):
    t.left(80)
    t.fd(100)
    t.left(135)
    t.fd(165)
    t.left(125)
    t.fd(115)
t.done()
'''
#t.goto(0,0)


'''
t.circle(90,45)

t.goto(0,90)
t.seth(0)
t.fd(90)
t.goto(0,90)
t.circle(90,45)


t.goto(90,90)
t.goto(0,90)
t.seth(45)
t.fd(90)



t.goto(150,0)
t.circle(45,150)
t.goto(0,0)


t.goto(0,150)
t.circle(45,150)
t.goto(0,0)

t.goto(-150,0)
t.circle(45,-150)
t.goto(0,0)

t.goto(0,-150)
t.circle(-45,-150)
t.goto(0,0)
'''
for i in range(4):
    t.fd(150)
    t.right(90)
    t.circle(-150,45)
    t.goto(0,0)
    t.left(45)
t.done()
