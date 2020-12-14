import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Game Timer Demo")

player = turtle.Turtle()
player.shape("triangle")
player.color("blue")
player.speed(0)
player.penup()

is_paused = False

def toggle_pause():
    global is_paused
    if is_paused == True:
        is_paused = False
    else:
        is_paused = True

wn.listen()
wn.onkey(toggle_pause, "p")

while True:
    if not is_paused:
        player.fd(1)
        player.lt(1)
    else:
        wn.update()
wn.mainloop()