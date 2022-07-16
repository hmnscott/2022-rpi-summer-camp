# Write your code here :-)
import random

WIDTH = 500
HEIGHT = 500

alien = Actor("alien")
alien.pos = (250, 250)
box = Rect((20, 20), (100, 100))

hits = 0

background = Actor("background")

def draw():
    screen.clear()
    background.draw()
    screen.draw.filled_rect(box, "red")
    alien.draw()

def update():
    if keyboard.q:
        exit()

    # alien movement
    if keyboard.right or keyboard.l:
        alien.x += 4
    elif keyboard.left or keyboard.h:
        alien.x -= 4
    elif keyboard.up or keyboard.k:
        alien.y -= 4
    elif keyboard.down or keyboard.j:
        alien.y += 4

    if alien.x > WIDTH:
        alien.x = 0
    if alien.x < 0:
        alien.x = 498
    if alien.y > HEIGHT:
        alien.y = 0
    if alien.y < 0:
        alien.y = 498

    if box.x + 50 < alien.x:
        box.x -= 1
    elif box.x + 50 > alien.x:
        box.x += 1
    if box.y + 50 < alien.y:
        box.y -= 1
    elif box.y + 50 > alien.y:
        box.y += 1



    if box.y > HEIGHT:
        box.y = random.randint(0, HEIGHT)
    if box.y < 0:
        box.y = random.randint(0, HEIGHT)
    if box.x > WIDTH:
        box.x = random.randint(0, WIDTH)
    if box.x < 0:
        box.x = random.randint(0, WIDTH)

    if alien.colliderect(box):
        global hits
        hits += 1
        print(f"Score: {hits}")
        box.x = random.randint(0, WIDTH)
        box.y = random.randint(0, HEIGHT)

