import turtle

t = turtle.Turtle()

for i in range(5):
    if i % 2 == 0:
        t.left(90)
    t.forward(50)

turtle.done()
