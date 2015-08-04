import turtle
t = turtle.Pen()

def pendulum():
    t.left(90)
    t.up()
    t.forward(100)
    t.right(90)
    t.down()
    t.circle(10)
    t.up()
    t.forward(150)
    t.right(90)

def swing(m1,m2):
    for x in range (1,5):
        m1 = m1 - 2
        m2 = m2 - 4
        t.circle(-150,m1)
        t.right(180)
        t.stamp()
        t.circle(150,m2)
        t.left(180)
        t.stamp()

pendulum()
swing(180,180)

