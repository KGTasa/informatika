import pygame
pygame.init()
(sirina,duzina)=(300,350)
prozor=pygame.display.set_mode((sirina, duzina))
pygame.display.set_caption("Figura")
prozor.fill(pygame.Color('White'))

#promenljive
(cx,cy)=(sirina//2, duzina//2)
pglava=50

#glava
pygame.draw.circle(prozor, pygame.Color('pink'), (150, 50), pglava)
pygame.draw.circle(prozor, pygame.Color('red'), (150, 50), pglava, 1)

#leva ruka
pygame.draw.rect(prozor, pygame.Color('pink'), (210, 100, 30, 100))
pygame.draw.rect(prozor, pygame.Color('red'), (210, 100, 30, 100), 1)

#desna ruka
pygame.draw.rect(prozor, pygame.Color('pink'), (60, 100, 30, 100))
pygame.draw.rect(prozor, pygame.Color('red'), (60, 100, 30, 100), 1)

#torso
pygame.draw.rect(prozor, pygame.Color('pink'), (90, 100, 120, 150))
pygame.draw.rect(prozor, pygame.Color('red'), (90, 100, 120, 150), 1)

#leva noga
pygame.draw.rect(prozor, pygame.Color('pink'), (160, 250, 40, 100))
pygame.draw.rect(prozor, pygame.Color('red'), (160, 250, 40, 100), 1)

#desna noga
pygame.draw.rect(prozor, pygame.Color('pink'), (100, 250, 40, 100))
pygame.draw.rect(prozor, pygame.Color('red'), (100, 250, 40, 100), 1)

pygame.display.update()
while pygame.event.wait().type !=pygame.QUIT:
   pass
pygame.quit()
