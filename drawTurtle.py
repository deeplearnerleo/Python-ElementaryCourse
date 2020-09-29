import turtle 
turtle.setup(1500,500,200,200)
turtle.penup()
turtle.fd(-650)
turtle.pendown()
turtle.pensize(2)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(6):
    turtle.circle(2,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)


turtle.done()
