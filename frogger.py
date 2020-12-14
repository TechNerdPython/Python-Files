import turtle
import math
import time
import random

# Set up the screen
wn = turtle.Screen()
wn.cv._rootwindow.resizable(False, False)
wn.title("Frogger by @BandaruLalith")
wn.setup(600, 800)
wn.bgcolor("green")
wn.bgpic("background.gif")
wn.tracer(0)

# Register shape
shapes = ["frog.gif", "car_left.gif", "car_right.gif", "log_full.gif", "turtle_left.gif",
          "turtle_right.gif", "turtle_left_half.gif", "turtle_right_half.gif", "turtle_submerged.gif", "home.gif",
          "frog_home.gif"]
for shape in shapes:
    wn.register_shape(shape)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()

# Create classes


class Sprite():
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.image)
        pen.stamp()

    def update(self):
        pass

    def is_collision(self, other):
        # Axis Aligned Bounding Box
        x_collision = (math.fabs(self.x - other.x) *
                       2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) *
                       2) < (self.height + other.height)
        return (x_collision and y_collision)


class Player(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = 0
        self.collision = False

    def up(self):
        self.y += 50

    def down(self):
        self.y -= 50

    def left(self):
        self.x -= 50

    def right(self):
        self.x += 50

    def update(self):
        self.x += self.dx

        # Border Checking
        if self.x < -250 or self.x > 250:
            self.x = 0
            self.y = -300


class Car(Sprite):
    def __init__(self, x, y, width, height, image, dx):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx

    def update(self):
        self.x += self.dx

        # Border Checking
        if self.x < -400:
            self.x = 400

        if self.x > 400:
            self.x = -400


class Log(Sprite):
    def __init__(self, x, y, width, height, image, dx):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx

    def update(self):
        self.x += self.dx

        # Border Checking
        if self.x < -400:
            self.x = 400

        if self.x > 400:
            self.x = -400


class Turtle(Sprite):
    def __init__(self, x, y, width, height, image, dx):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx
        self.state = "full"  # Half, Submerged
        self.full_time = random.randint(8, 12)
        self.half_time = random.randint(4, 6)
        self.submerged_time = random.randint(4, 6)
        self.start_time = time.time()

    def update(self):
        self.x += self.dx

        # Border Checking
        if self.x < -400:
            self.x = 400

        if self.x > 400:
            self.x = -400

        # Update image based on state
        if self.state == "full":
            if self.dx > 0:
                self.image = "turtle_right.gif"
            else:
                self.image = "turtle_left.gif"
        elif self.state == "half_up" or self.state == "half_down":
            if self.dx > 0:
                self.image = "turtle_right_half.gif"
            else:
                self.image = "turtle_left_half.gif"
        elif self.state == "submerged":
            self.image = "turtle_submerged.gif"

        # Timer stuff
        if self.state == "full" and time.time() - self.start_time > self.full_time:
            self.state = "half_down"
            self.start_time = time.time()
        elif self.state == "half_down" and time.time() - self.start_time > self.half_time:
            self.state = "submerged"
            self.start_time = time.time()
        elif self.state == "submerged" and time.time() - self.start_time > self.submerged_time:
            self.state = "half_up"
            self.start_time = time.time()
        elif self.state == "half_up" and time.time() - self.start_time > self.half_time:
            self.state = "full"
            self.start_time = time.time()


class Home(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = 0


# Create objects
player = Player(0, -300, 40, 40, "frog.gif")
car_left = Car(0, -250, 121, 40, "car_left.gif", -0.05)
car_right = Car(0, -200, 121, 40, "car_right.gif", 0.1)
log_left = Log(0, 100, 121, 40, "log_full.gif", -0.2)
log_right = Log(0, 50, 121, 40, "log_full.gif", 0.2)
turtle_left = Turtle(0, 200, 250, 40, "turtle_left.gif", -0.15)
turtle_right = Turtle(0, 150, 155, 40, "turtle_right.gif", 0.15)

car_left2 = Car(0, -150, 121, 40, "car_left.gif", -0.1)
car_right2 = Car(0, -100, 121, 40, "car_right.gif", 0.1)
car_left3 = Car(0, -50, 121, 40, "car_left.gif", -0.1)
log_right2 = Log(0, 250, 250, 40, "log_full.gif", 0.2)

home1 = Home(0, 300, 50, 50, "home.gif")
home2 = Home(-100, 300, 50, 50, "home.gif")
home3 = Home(-200, 300, 50, 50, "home.gif")
home4 = Home(100, 300, 50, 50, "home.gif")
home5 = Home(200, 300, 50, 50, "home.gif")

# Create a list of sprites
sprites = [car_left, car_right, log_right, log_left, turtle_left,
           turtle_right, car_left2, car_left3, car_right2, log_right2, home1, home2, home3, home4, home5]
sprites.append(player)

# Keyboard binding
wn.listen()
wn.onkeypress(player.up, "Up")
wn.onkeypress(player.down, "Down")
wn.onkeypress(player.left, "Left")
wn.onkeypress(player.right, "Right")

# Main Game Loop
while True:
    # Render
    for sprite in sprites:
        sprite.render(pen)
        sprite.update()

    # Check for collisions
    player.dx = 0
    player.collision = False
    for sprite in sprites:
        if player.is_collision(sprite):
            if isinstance(sprite, Car):
                player.x = 0
                player.y = -300
                break
            elif isinstance(sprite, Log):
                player.dx = sprite.dx
                player.collision = True
                break
            elif isinstance(sprite, Turtle) and sprite.state != "submerged":
                player.dx = sprite.dx
                player.collision = True
                break
            elif isinstance(sprite, Home):
                player.x = 0
                player.y = -300
                sprite.image = "frog_home.gif"
                break

    # Check if we are not touching above y = 0
    if player.y > 0 and player.collision != True:
        player.x = 0
        player.y = -300

    # Update the Screen
    wn.update()

    # Clear the screen
    pen.clear()

wn.mainloop()
