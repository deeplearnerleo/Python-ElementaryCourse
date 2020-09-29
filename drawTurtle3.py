import turtle as t
t.setup(1000,1000)
t.penup()
t.down()
t.pensize(20)
t.pencolor("black")

t.fd(100)


for i in range(1,6):
    j = i*60
    t.seth(j)
    t.fd(100)
t.done()


'''
t.seth(60)
t.fd(100)

t.seth(120)
t.fd(100)

t.seth(180)
t.fd(100)

t.seth(240)
t.fd(100)

t.seth(300)
t.fd(100)
t.done()
'''
