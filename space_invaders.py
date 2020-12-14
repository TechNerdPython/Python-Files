import turtle
import os
import math
import random

# Set up the Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders by @lalithbandaru")
wn.bgpic("space_invaders_background.gif")

# Register the Shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")
# Draw Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Set the score to 0
score = 0

# Draw the Score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
score_string = "Score: %s" %score
score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Create the Player Turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

player_speed = 15

# Create a number of enemies
number_of_enemies = 5
# Create an empty list of enemies
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
    # Create the Enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x, y)

enemy_speed = 2

# Create the Player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bullet_speed = 20

# Define bullet state
# ready - ready to fire
# fire - bullet is firing
bullet_state = "ready"

# Move the Player Left and Right
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    # Declare bulletstate as a global if it needs to be changed
    global bullet_state

    if bullet_state == "ready":
        bullet_state = "fire"
        # Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollison(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()- t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False
    
# Keyboard Bindings
turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(fire_bullet, "space")

# Main Game Loop
while True:
    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        # Move the enemy back and down
        if enemy.xcor() > 280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemy_speed *= -1                  
                
        if enemy.xcor() < -280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemy_speed *= -1

        # Check for a collision between bullet and the enemy
        if isCollison(bullet, enemy):
            # Reset the Bullet
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.setposition(0,-400)
            x = random.randint(-200,200)
            y = random.randint(100,250)
            enemy.setposition(x, y)

            # Update the Score
            score += 10
            score_string = "Score: %s" %score
            score_pen.clear()
            score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))
        if isCollison(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over!")
            break
    # Move the bullet    
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # Check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"

