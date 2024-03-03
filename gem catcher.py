import pygame
import random
import time

HEIGHT = 700
WIDTH = 500
CENTER = WIDTH/2
score = 0
game_over = False

'''Player'''
player = Actor('idle')
player.pos= midbottom=(WIDTH/2 , 605)
player.speed = 5
player.frame = 1

def player_animate():

    if player.frame < 2:
        player.frame += 0.25
    else:
        player.frame = 1

    player.image = 'walk'+str(int(player.frame))

def player_move():
    if game_over ==False:
        player.image = 'idle'
    if keyboard.left and player.left > 0:
        player_animate()
        player.x -= player.speed
    elif keyboard.right and player.right < WIDTH:
        player_animate()
        player.x += player.speed


'''Gems'''
gems = []
number_of_gems = 5

def gem_spawn():
    gems.append(Actor('gem', pos = (random.randint(0, WIDTH - 30), 50)))

for i in range(number_of_gems):
    clock.schedule(gem_spawn, i)

def fall(gem):
    if gem.y < 620:
        gem.angle += 2
        gem.y += 4

'''Blades'''
blades = []
number_of_blades = 2

def blades_spawn():
    blades.append(Actor('blade', pos=(random.randint(0,WIDTH),0)))

def fall_blade(blade):
    if blade.y > HEIGHT:
        blade.pos = (random.randint(0,WIDTH),0)
    blade.angle += 3
    blade.y += 2

for i in range(number_of_blades):
    clock.schedule(blades_spawn, i * 5)


#DRAW
def draw():
    screen.fill((0,100,200))
    for i in range(8):
        screen.blit(images.ground, (i * images.ground.get_width(),HEIGHT - images.ground.get_height()))
    screen.draw.text("Score:" + str(score), midtop = (CENTER,0), fontname='mini_square', fontsize=36)
    screen.draw.text("Dodge the blades and grab the gems", midbottom = (CENTER, HEIGHT - 15),fontname='mini_square', fontsize=14)

    player.draw()
    if game_over == False:
        for gem in gems:
            gem.draw()
        for blade in blades:
            blade.draw()
    else:
        player.image = 'hit'
        music.fadeout(2.0)
        screen.draw.text("Game Over", center=(CENTER,HEIGHT/2), fontname='mini_square', fontsize=64)
#UPDATE
def update():
    global player_move, score, game_over


    if game_over == False:
        player_move()
        for gem in gems:
            fall(gem)

            if player.colliderect(gem):
                score += 1

                gem.pos = (random.randint(0,WIDTH), 50)

        for blade in blades:
            fall_blade(blade)
            if player.colliderect(blade):
                game_over = True