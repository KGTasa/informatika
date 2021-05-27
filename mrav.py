import pygame
pygame.init()
prozor=pygame.display.set_mode((300,300))
pygame.display.set_caption('Mrav')
prozor.fill(pygame.Color('White'))

pygame.draw.ellipse(prozor, pygame.Color('limegreen'), (75,100,150,180))
pygame.draw.line(prozor, pygame.Color('limegreen'), (130,110), (120,20), 6)
pygame.draw.line(prozor, pygame.Color('limegreen'), (170,110), (180,20), 6)
pygame.draw.circle(prozor, pygame.Color('limegreen'), (120,20), 10)
pygame.draw.circle(prozor, pygame.Color('limegreen'), (180,20), 10)
pygame.draw.ellipse(prozor, pygame.Color('black'), (110,140,30,50))
pygame.draw.ellipse(prozor, pygame.Color('black'), (160,140,30,50))

pygame.display.update()
while pygame.event.wait().type!=pygame.QUIT:
    pass
pygame.quit()