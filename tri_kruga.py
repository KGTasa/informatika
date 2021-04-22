import pygame
pygame.init()
(sirina,duzina)=(400,400)
prozor=pg.display.set_mode((sirina, duzina))
pygame.display.set_caption("Tri Kruga")
prozor.fill(pg.Color('White'))

(cx,cy)=(sirina//2, duzina//2)
poluprecnik1=125
poluprecnik2=100
poluprecnik3=75

pg.draw.circle(prozor, pg.Color('black'), (cx, cy), poluprecnik1, 2)
pg.draw.circle(prozor, pg.Color('yellow'), (cx, cy), poluprecnik2, 2)
pg.draw.circle(prozor, pg.Color('green'), (cx, cy), poluprecnik3, 2)

pygame.display.update()
while pygame.event.wait().type !=pygame.QUIT:
   pass
pygame.quit()
