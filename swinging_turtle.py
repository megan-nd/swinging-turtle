import turtle
t = turtle.Pen()

def pendulum():
    t.shape('turtle')
    t.color('dark green')
    t.left(90)
    t.up()
    t.forward(100)
    t.right(90)
    t.down()
    t.circle(10)
    t.up()
    t.forward(150)
    t.right(90)

def swing(m):
    for x in range (1,23):
        m = m - 8
        t.circle(-150,m)
        t.right(180)
        #t.stamp()
        t.circle(150,m - 4)
        t.left(180)
        #t.stamp()
    t.left(90)
        
pendulum()
swing(180)

