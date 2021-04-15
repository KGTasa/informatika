import pygame
pygame.init()
pygame.display.set_caption("zadatak1")
prozor=pygame.display.set_mode((350,150))
prozor.fill(pygame.Color("white"))
pygame.draw.rect(prozor, pygame.Color("red"),(50,50,50,50))
pygame.draw.rect(prozor, pygame.Color("green"),(100,50,50,50))
pygame.draw.rect(prozor, pygame.Color("blue"),(150,50,50,50))
pygame.draw.rect(prozor, pygame.Color("black"),(200,50,50,50))
pygame.draw.rect(prozor, pygame.Color("yellow"),(250,50,50,50))
pygame.display.update()
while pygame.event.wait().type !=pygame.QUIT:
    pass
pygame.quit()
