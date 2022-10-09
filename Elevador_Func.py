import pygame
from pygame.locals import *
from sys import exit

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('sounds/kudasai-technicolor.wav')
pygame.mixer.music.play(-1)

width = 640
height = 480
y = 280
destiny = 0
floor = 280
e_height = 30
blue = (0, 0, 255)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
font = pygame.font.SysFont('Arial', 14, True, True)

state = [()]
clock = pygame.time.Clock()
tela = pygame.display.set_mode((width, height))
pygame.display.set_caption('elevator')
text = [0, 1, 2, 3, 4, 5, 6, 7]
line = [0, 1, 2, 3, 4, 5, 6, 7]
s_width = []
string = 'states: q0'

# game script
while True:
    tela.fill(black)
    # frames per second game
    e_height = 30

    i = 0
    while i < 8:
        text[i] = font.render(f'ANDAR {i}: ', True, white)
        i = i + 1

    new_text = font.render(string, True, white)
    red_block = pygame.draw.rect(tela, red, (70, y, 30, e_height))
    text_x = 0
    text_y = 280
    
    for i in range(8):
        tela.blit(text[i], (text_x, text_y))
        text_y = text_y - 40

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_7:
                destiny = 0 - y
                floor = 0
                string = string + ' ' + 'q7'
            if event.key == K_6:
                destiny = 40 - y
                floor = 40
                string = string + ' ' + 'q6'
            if event.key == K_5:
                destiny = 80 - y
                floor = 80
                string = string + ' ' + 'q5'
            if event.key == K_4:
                destiny = 120 - y
                floor = 120
                string = string + ' ' + 'q4'
            if event.key == K_3:
                destiny = 160 - y
                floor = 160
                string = string + ' ' + 'q3'
            if event.key == K_2:
                destiny = 200 - y
                floor = 200
                string = string + ' ' + 'q2'
            if event.key == K_1:
                destiny = 240 - y
                floor = 240
                string = string + ' ' + 'q1'
            if event.key == K_0:
                floor = 280
                destiny = 280 - y
                string = string + ' ' + 'q0'
            if event.key == K_SPACE:
                exit()
    tela.blit(new_text, (0, 460))
    if destiny < 0:          
        while y != floor:
            pygame.display.update()
            tela.fill(black)
            i = 0
            while i < 8:
                text[i] = font.render(f'ANDAR {i}: ', True, white)
                i = i + 1

            new_text = font.render(string, True, white)
            red_block = pygame.draw.rect(tela, red, (70, y, 30, e_height))
            text_x = 0
            text_y = 280
    
            for i in range(8):
                tela.blit(text[i], (text_x, text_y))
                text_y = text_y - 40
            tela.blit(new_text, (0, 460))
            red_block = pygame.draw.rect(tela, blue, (70, y, 30, e_height))
            y = y - 1
            clock.tick(40)
    else:
        while y != floor:
            pygame.display.update()
            tela.fill(black)
            i = 0
            while i < 8:
                text[i] = font.render(f'ANDAR {i}: ', True, white)
                i = i + 1

            new_text = font.render(string, True, white)
            red_block = pygame.draw.rect(tela, red, (70, y, 30, e_height))
            text_x = 0
            text_y = 280
    
            for i in range(8):
                tela.blit(text[i], (text_x, text_y))
                text_y = text_y - 40
            tela.blit(new_text, (0, 460))
            red_block = pygame.draw.rect(tela, blue, (70, y, 30, e_height))
            y = y + 1
            clock.tick(40)

    pygame.display.flip()
