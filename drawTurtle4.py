import turtle as t
t.setup(1000,1000)
t.penup()
t.pendown()
t.pensize(2)
t.pencolor("black")

t.fd(100)

for i in range(1,9):
    j = i*80
    t.seth(j)
    t.fd(100)

t.done()
