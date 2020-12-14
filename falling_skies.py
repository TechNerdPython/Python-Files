import turtle
import random

wn = turtle.Screen()
wn.title("Falling Skies by @lalithbandaru")
wn.bgcolor("green")
wn.setup(800, 600)
wn.tracer(0)

# Score
score = 0

# Lives
lives = 3

# Add the Player
player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"

# Creating the Acorns
acorns = []

for _ in range(20):
    # Add the Acorn
    acorn = turtle.Turtle()
    acorn.speed(0)
    acorn.shape("circle")
    acorn.color("yellow")
    acorn.penup()
    acorn.goto(0, 250)
    acorn.speed = random.randint(1, 4)
    acorns.append(acorn)

# Creating the Hunters
hunters = []

for _ in range(20):
    # Add the Hunters
    hunter = turtle.Turtle()
    hunter.speed(0)
    hunter.shape("circle")
    hunter.color("red")
    hunter.penup()
    hunter.goto(0, 250)
    hunter.speed = random.randint(1, 4)
    hunters.append(hunter)

# Make the Pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

# Functions
def go_left():
    player.direction = "left"

def go_right():
    player.direction = "right"

# Keyboard Bindings
wn.listen()
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")


# Main Game Loop
while True:
    # Update the Screen
    wn.update()
    
    # Move the Player
    if player.direction == "left":
        x = player.xcor()
        x -= 2
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += 2    
        player.setx(x)

    for acorn in acorns:
        # Move the Acorn
        y = acorn.ycor()
        y -= acorn.speed
        acorn.sety(y)

        # Check if off the screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            acorn.goto(x, y)

        # Check for a collision between the player and the acorn
        if acorn.distance(player) < 20:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            acorn.goto(x, y)
            score += 10
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
    
    for hunter in hunters:
        # Move the Hunter
        y = hunter.ycor()
        y -= hunter.speed
        hunter.sety(y)

        # Check if off the screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            hunter.goto(x, y)

        # Check for a collision between the player and the hunter
        if hunter.distance(player) < 20:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            hunter.goto(x, y)
            score -= 10
            lives -= 1
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
wn.mainloop()