import pygame
pygame.init()
prozor=pygame.display.set_mode((200,200))
pygame.display.set_caption('Isprekidana linija')
prozor.fill(pygame.Color('yellow'))
pygame.draw.rect(prozor, pygame.Color('red'), (5, 90, 30, 10))
pygame.draw.rect(prozor, pygame.Color('green'), (45, 90, 30, 10))
pygame.draw.rect(prozor, pygame.Color('blue'), (85, 90, 30, 10))
pygame.draw.rect(prozor, pygame.Color('magenta'), (125, 90, 30, 10))
pygame.draw.rect(prozor, pygame.Color('cyan'), (165, 90, 30, 10))
pygame.display.update()
while pygame.event.wait().type!=pygame.QUIT:
    pass
pygame.quit()