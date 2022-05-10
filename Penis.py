import turtle
t = turtle.Turtle()

screen = turtle.Screen()

# Balls
t.circle(50)
t.penup()
t.setpos(100, 0)
t.pendown()
t.circle(50)

# Rest of Penis
t.penup()
t.setpos(0, 100)
t.pendown()
t.lt(90)
t.fd(200)
t.rt(90)
t.fd(100)
t.lt(90)
t.circle(radius=50, extent=180)
t.setpos(100.00, 300.00)
t.fd(200)
t.penup()
t.setpos(50, 350)
t.pendown()
t.rt(180)
t.circle(radius=50, extent=90)
turtle.done()
