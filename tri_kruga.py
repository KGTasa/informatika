import pygame
pygame.init()
(sirina,duzina)=(400,400)
prozor=pygame.display.set_mode((sirina, duzina))
pygame.display.set_caption("Tri Kruga")
prozor.fill(pygame.Color('White'))

(cx,cy)=(sirina//2, duzina//2)
poluprecnik1=125
poluprecnik2=100
poluprecnik3=75

pygame.draw.circle(prozor, pygame.Color('black'), (cx, cy), poluprecnik1, 2)
pygame.draw.circle(prozor, pygame.Color('yellow'), (cx, cy), poluprecnik2, 2)
pygame.draw.circle(prozor, pygame.Color('green'), (cx, cy), poluprecnik3, 2)

pygame.display.update()
while pygame.event.wait().type !=pygame.QUIT:
   pass
pygame.quit()
