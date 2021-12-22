import pygame
from pygame.draw import *

pygame.init()

FPS = 30
width, height = int(input()), int(input())
if width < 600:
    width = 600
if height < 800 or height > 1000:
    height = 800
screen = pygame.display.set_mode((width, height))
#ФОН
rect(screen, (0, 230, 230), (0, 0, width, height))
rect(screen, (0, 255, 0), (0, height//2, width, height)),
#дерево
def tree(x=0):
    rect(screen, (255, 255, 255), (70, 470, 40+x, 120+x))
    ellipse(screen, (0, 155, 100), (25, 400, 130+x, 100+x))
    ellipse(screen, (0, 155, 100), (-10, 270, 200+x, 160+x))
    ellipse(screen, (0, 155, 100), (15, 180, 150+x, 120+x))
    ellipse(screen, (250, 200, 100), (30, 240, 20+x, 20+x))
    ellipse(screen, (250, 200, 100), (140, 300, 20+x, 20+x))
    ellipse(screen, (250, 200, 100), (50, 400, 20+x, 20+x))
    ellipse(screen, (250, 200, 100), (130, 450, 20+x, 20+x))
#Солнце
def sun(x=0):
    circle(screen, (255, 255, 0), (width-20, 20), 150+x)

#Единорог без гривы
def horse(x=0):
    ellipse(screen, (255, 255, 255), (360, 500, 200+x, 100+x))
    rect(screen, (255, 255, 255), (460, 420, 80+x, 120+x))
    rect(screen, (255, 255, 255), (380, 570, 30+x, 100+x))
    rect(screen, (255, 255, 255), (420, 550, 24+x, 100+x))
    rect(screen, (255, 255, 255), (470, 570, 30+x, 100+x))
    rect(screen, (255, 255, 255), (510, 550, 24+x, 100+x))
    ellipse(screen, (255, 255, 255), (480, 400, 100+x, 50+x))
    ellipse(screen, (255, 255, 255), (470, 380, 70+x, 50+x))
#РОГ
def rog(x=0):
    polygon(screen, (255, 160, 255), [(500+x,390+x), (530+x,400+x),
                               (550+x,300+x)])
#глаза и рот
def eyesmouth(x=0):
    ellipse(screen, (151, 100, 255), (500, 400, 20+x, 20+x))
    ellipse(screen, (0, 0, 0), (510, 405, 7+x, 7+x))
    ellipse(screen, (255, 255, 255), (500, 405, 10+x, 7+x))
#грива
def griva(x=0):
    ellipse(screen, (167, 130, 255), (451, 370, 70+x, 30+x))
    ellipse(screen, (167, 130, 255), (431, 380, 70+x, 30+x))
    ellipse(screen, (167, 130, 255), (423, 400, 70+x, 30+x))
    ellipse(screen, (167, 130, 255), (421, 422, 70+x, 30+x))
    ellipse(screen, (167, 130, 255), (421, 432, 70+x, 30+x))
    ellipse(screen, (167, 130, 255), (411, 452, 70+x, 30+x))
    ellipse(screen, (167, 130, 255), (401, 472, 70+x, 30+x))
    ellipse(screen, (167, 130, 255), (391, 492, 70+x, 30+x))
    ellipse(screen, (167, 130, 255), (381, 502, 70+x, 30+x))
#хвост
def tail(x=0):
    ellipse(screen, (167, 130, 255), (310, 530, 70+x, 30+x))
    ellipse(screen, (167, 130, 255), (300, 540, 60+x, 30+x))
    ellipse(screen, (167, 130, 255), (290, 555, 60+x, 30+x))


tree(10)
sun(20)
horse(20)
rog(20)
eyesmouth(20)
griva(20)
tail(20)




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()