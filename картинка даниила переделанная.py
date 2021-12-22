import pygame
from pygame.draw import *
from pygame.transform import *

pygame.init()
width = int(input())
height = int(input())
if height < 800 or height > 1100:
    height = 800
if width < 1200 or width > 1400:
    width = 1200
FPS = 30
screen = pygame.display.set_mode((width, height))
# фон
rect(screen, (170, 238, 255), (0, 0, width, height/2))
rect(screen, (55, 200, 113), (0, height/2, width, height/2))

def men():
    #мужчина
    surf = pygame.Surface((700, 800), pygame.SRCALPHA) #тело
    ellipse(surf, (167, 147, 172), (100, 195, 120, 230))
    surf = rotate(surf, 0)
    screen.blit(surf, (50, 100))
    #голова
    circle(screen, (244, 227, 215), (210, 260), 50)
    #руки и ноги
    line(screen, (0, 0, 0), (175, 320), (70, 450), 1)
    line(screen, (0, 0, 0), (245, 320), (340, 450), 1)
    line(screen, (0, 0, 0), (190, 515), (140, 660), 1)
    line(screen, (0, 0, 0), (235, 510), (265, 660), 1)
    line(screen, (0, 0, 0), (140, 660), (110, 662), 1)
    line(screen, (0, 0, 0), (265, 660), (295, 662), 1)

def second_man():
    #мужчина
    ellipse(screen, (167, 147, 172), (100+840, 290, 120, 230))
    #голова
    circle(screen, (244, 227, 215), (210+790, 260), 50)
    #руки и ноги
    line(screen, (0, 0, 0), (175+790, 320), (70+790, 450), 1)
    line(screen, (0, 0, 0), (245+794, 320), (340+794, 450), 1)
    line(screen, (0, 0, 0), (190+794, 515), (140+794, 660), 1)
    line(screen, (0, 0, 0), (235+790, 510), (265+790, 660), 1)
    line(screen, (0, 0, 0), (140+794, 660), (110+794, 662), 1)
    line(screen, (0, 0, 0), (265+790, 660), (295+790, 662), 1)


def bouquet():
    polygon(screen, (255, 204, 0), [[1075+60, 450], [1120+60, 410], [1070+60, 380]])
    # aalines(screen, (255, 204, 0), True, [[75, 450], [20, 410], [70, 380]])
    circle(screen, (85, 0, 0), (1075+70, 390), 16)
    circle(screen, (255, 0, 0), (1075+95, 400), 16)
    circle(screen, (255, 255, 255), (1075+90, 380), 16)

    line(screen, (0, 0, 0), (175 + 425, 330), (195 + 425, 150), 1)
    polygon(screen, (255, 204, 0), [[195 + 425, 150], [195 + 460, 80], [195 + 395, 70]])
    # aalines(screen, (255, 204, 0), True, [[75, 450], [20, 410], [70, 380]])
    circle(screen, (85, 0, 0), (195 + 410, 70), 18)
    circle(screen, (255, 0, 0), (195 + 430, 60), 20)
    circle(screen, (255, 255, 255), (195 + 450, 70), 18)

def woman():
    polygon(screen, (255, 85, 221), [[450, 270], [360, 540], [540, 540]])
    aalines(screen, (255, 85, 221), True, [[450, 270], [360, 540], [540, 540]])
    circle(screen, (244, 227, 215), (450, 270), 50)
    #руки и ноги
    line(screen, (0, 0, 0), (430, 330), (340, 450), 1)
    line(screen, (0, 0, 0), (470, 330), (530, 370), 1)
    line(screen, (0, 0, 0), (530, 370), (600, 330), 1)
    line(screen, (0, 0, 0), (420, 540), (420, 660), 1)
    line(screen, (0, 0, 0), (480, 540), (480, 660), 1)
    line(screen, (0, 0, 0), (420, 660), (390, 661), 1)
    line(screen, (0, 0, 0), (480, 660), (510, 661), 1)


def second_woman():
    polygon(screen, (255, 85, 221), [[450+300, 270], [360+300, 540], [540+300, 540]])
    aalines(screen, (255, 85, 221), True, [[450+300, 270], [360+300, 540], [540+300, 540]])
    circle(screen, (244, 227, 215), (450+300, 270), 50)
    #руки и ноги
    line(screen, (0, 0, 0), (340+430, 330), (430+430, 450), 1)
    line(screen, (0, 0, 0), (470+130, 330), (530+130, 370), 1)
    line(screen, (0, 0, 0), (530+130, 370), (600+130, 330), 1)
    line(screen, (0, 0, 0), (420+300, 540), (420+300, 660), 1)
    line(screen, (0, 0, 0), (480+300, 540), (480+300, 660), 1)
    line(screen, (0, 0, 0), (420+300, 660), (390+300, 661), 1)
    line(screen, (0, 0, 0), (480+300, 660), (510+300, 661), 1)

def ball():
    line(screen, (0, 0, 0), (70, 450), (50, 330), 1)
    polygon(screen, (255, 0, 0), [[50, 330], [20, 270], [70, 280]])
    # aalines(screen, (255, 0, 0), True, [[620, 240], [600, 180], [650, 190]])
    circle(screen, (255, 0, 0), (35, 270), 15)
    circle(screen, (255, 0, 0), (60, 270), 15)

men()
woman()
ball()
second_woman()
second_man()
bouquet()

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()