import pgzrun
import random

WIDTH = 800
HEIGHT = 600

bg = Actor("background")

ship = Actor('ship')
ship.x = 400
ship.y = 550

extrapoint = Actor('extrapoint')
extrapoint.x = random.randint(20, 780)
extrapoint.y = 0

enemy = Actor('enemy')
enemy.x = random.randint(20, 780)
enemy.y = 0

asteroid = Actor('asteroid')
asteroid.x = random.randint(20, 780)
asteroid.y = 0

score = 0
lives = 3
game_over = False
deathsound = False

print('Recorde: ', score)
print('Vidas: ', lives)

def update():
    global score, lives, game_over, deathsound

    if keyboard.left and ship.x > 30:
        ship.x -= 5
    elif keyboard.right and ship.x < 770:
        ship.x += 5

    extrapoint.y += 4 + score / 5
    if extrapoint.y > 600:
        extrapoint.x = random.randint(20,700)
        extrapoint.y = 0

    if extrapoint.colliderect(ship):
        sounds.collect.play()
        extrapoint.x = random.randint(20,700)
        extrapoint.y = 0
        score += 1
        print('Recorde: ', score)

    asteroid.y += 4
    if asteroid.y > 600:
        asteroid.x = random.randint(20,700)
        asteroid.y = 0

    if asteroid.colliderect(ship):
        sounds.losing.play()
        asteroid.x = random.randint(20,700)
        asteroid.y = 0
        score -= 1 if score > 0 else 0
        print('Recorde: ', score)

    enemy.y += 5
    if enemy.y > 600:
        enemy.x = random.randint(20,700)
        enemy.y = 0

    if enemy.colliderect(ship):
        sounds.explosion.play()
        enemy.x = random.randint(20,700)
        enemy.y = 0
        lives -= 1 if lives > 0 else 0
        print('Vidas: ', lives)

    if lives == 0:
        game_over = True
        deathsound = True
        extrapoint.y = 0
        enemy.y = 0
        asteroid.y = 0
        if deathsound == False:
            sounds.losing.play()
        deathsound = True

def draw():
    bg.draw()

    if game_over:
        screen.draw.text('FIM DE JOGO', (230, 200), color="white", fontname='publicpixel', fontsize=30)
        screen.draw.text('RECORDE FINAL: ' + str(score), (180, 300), color="lightblue", fontname='publicpixel', fontsize=15)
    else:
        ship.draw()
        extrapoint.draw()
        enemy.draw()
        asteroid.draw()
        screen.draw.text('Recorde: ' + str(score), (15, 10), color="lightblue", fontname='publicpixel', fontsize=15)
        screen.draw.text('Vidas: ' + str(lives), (665, 10), color="yellow", fontname='publicpixel', fontsize=15)
