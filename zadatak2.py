import pygame
pygame.init()
pygame.display.set_caption("zadatak2")
prozor=pygame.display.set_mode((500,500))
prozor.fill(pygame.Color("white"))
pygame.draw.rect(prozor, pygame.Color("orange"),(50,50,400,400))
pygame.draw.rect(prozor, pygame.Color("black"), (150,150,50,50))
pygame.draw.rect(prozor, pygame.Color("black"), (300,150,50,50))
pygame.draw.rect(prozor, pygame.Color("black"), (200,300,100,100))
pygame.display.update()
while pygame.event.wait().type !=pygame.QUIT:
    pass
pygame.quit()
