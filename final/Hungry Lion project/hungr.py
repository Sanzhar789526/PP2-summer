import sys
from pygame.locals import *
import pygame as pgm
import random

white = (255, 255, 255)
black = (0,   0,   0  )
red   = (255, 0,   0  )
green = (0,   255, 0  )
blue  = (0,   0,   255) 

pgm.init()
pgm.mixer.init()

screen = pgm.display.set_mode((800, 600))
pgm.display.set_caption("HUNGRY LION")

FPS = 60
clock = pgm.time.Clock()

x, y = 100, 100
dx, dy = 5, 5



#класс для игры 
class Player:
    def __init__(self):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.color = blue
    def move(self):
        pass
    def draw(self):
        self.rect = Rect(self.x, self.y, self.width, self.height)
        pgm.draw.rect(screen, self.color, self.rect)
#класс для еды
class Food:
    def __init__(self, where1):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 800)
        self.y2 = 620
        self.x2 = random.randint(0, 800)
        self.dy = 1
        self.color = green
        self.width = 30
        self.height = 20
        self.where = where1
        self.rect = Rect(self.x, self.y, self.width, self.height)
    def move(self):
        self.y -= self.dy
        if self.y < -20:
            self.y = random.randint(620, 640)
            self.x = random.randint(0, 770)
        self.y2 -= self.dy
        if self.y2 < -20:
            self.y2 = random.randint(620, 640)
            self.x2 = random.randint(0, 770)
    def draw(self):
        if self.where == True:
            self.rect = Rect(self.x, self.y, self.width, self.height)
            pgm.draw.rect(screen, self.color, self.rect)
        if self.where == False:
            self.rect = Rect(self.x2, self.y2, self.width, self.height)
            pgm.draw.rect(screen, self.color, self.rect)
#класс для враги
class Enemy:
    def __init__(self, where2):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 800)
        self.y2 = -20
        self.x2 = random.randint(0, 800)
        self.dy = 1.5
        self.width = 30
        self.height = 20
        self.color = red
        self.where = where2
        self.rect = Rect(self.x, self.y, self.width, self.height)
    def move(self):
        self.y += self.dy
        if self.y > 600: 
            self.y = random.randint(-40, -20)
            self.x = random.randint(0, 770)
        self.y2 += self.dy
        if self.y2 > 600:
            self.y2 = random.randint(-40, -20)
            self.x2 = random.randint(0, 770)
    def draw(self):
        if self.where == True:
            self.rect = Rect(self.x, self.y, self.width, self.height)
            pgm.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        elif self.where == False:
            self.rect = Rect(self.x2, self.y2, self.width, self.height)
            pgm.draw.rect(screen, self.color, (self.rect))


enemies = []
foods = []
playerman = Player()

for i in range(10):
    food = Food(True)
    foods.append(food)
for i in range(20):
    enemy = Enemy(True)
    enemies.append(enemy)


running = True

score = 0
while running:
    for event in pgm.event.get():
        if event.type == pgm.QUIT:
            sys.exit()
            running = False
    where1 = True
    where2 = True
    pressed = pgm.key.get_pressed()
    if pressed[pgm.K_RIGHT]: playerman.x += dx 
    if pressed[pgm.K_LEFT]: playerman.x -= dx
    if pressed[pgm.K_DOWN]: playerman.y += dy 
    if pressed[pgm.K_UP]: playerman.y -= dy
        
    if playerman.x <= 0: playerman.x = 0
    if playerman.x >= 780: playerman.x = 780
    if playerman.y <= 0: playerman.y = 0
    if playerman.y >= 580: playerman.y = 580

    for food in foods:
        food.move()
    for enemy in enemies:
        enemy.move()

    screen.fill(white)

    playerman.move()
    playerman.draw()

    for enemy in enemies:
        if pgm.Rect.colliderect(playerman.rect, enemy.rect):
            score -= 1
            enemies.remove(enemy)
            x = Enemy(False)
            enemies.append(x)
            
    for food in foods:
        if pgm.Rect.colliderect(playerman.rect, food.rect):
            score += 1
            foods.remove(food)
            x = Food(False)
            y = Enemy(False)
            foods.append(x)
            enemies.append(y)
            
    for food in foods:
        food.x += random.randint(-2, 2)
        food.y += random.randint(-2, 2)
        food.x2 += random.randint(-2, 2)
        food.y2 += random.randint(-2, 2)
            
    for food in foods:
        food.draw()
    for enemy in enemies:
        enemy.draw()
    s_score = 'Score: ' + str(score)
    font = pgm.font.Font('freesansbold.ttf', 32)
    text = font.render(s_score, True, black)
    textRect = text.get_rect()
    textRect.topleft = (10, 10) 
    screen.blit(text, textRect)

    pgm.display.flip()
    clock.tick(FPS)

pgm.quit()
 