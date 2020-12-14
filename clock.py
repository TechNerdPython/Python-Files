import turtle
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Simple Analog Clock by @lalithbandaru")
wn.tracer(0)

# Create our drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(h, min, sec, pen):
    # Draw Clock Face
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("blue")
    pen.pendown()
    pen.circle(210)

    # Draw the Increments for the hours
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)

    # Draw the Hour Hand
    pen.penup()
    pen.goto(0,0)
    pen.color("white")
    pen.setheading(90)
    angle = (h / 12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    # Draw the Minute Hand
    pen.penup()
    pen.goto(0,0)
    pen.color("red")
    pen.setheading(90)
    angle = (min / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(170)

    # Draw the Second Hand
    pen.penup()
    pen.goto(0,0)
    pen.color("yellow")
    pen.setheading(90)
    angle = (sec / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(50)

while True:
    h = int(time.strftime("%I"))
    min = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))

    draw_clock(h, min, sec, pen)
    
    wn.update()
    
    time.sleep(1)

    pen.clear()

wn.mainloop()