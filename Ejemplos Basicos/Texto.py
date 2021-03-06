import pygame

NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)

dimensiones = (400, 500)
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Manejo de texto")

reloj = pygame.time.Clock()

game_over = False
contador = 0
while not game_over:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_over = True
    contador += 1
    pantalla.fill((255, 255, 255))
    pygame.font.init()
    fuente = pygame.font.Font("AliceandtheWickedMonster.ttf", 50)
    Texto = fuente.render(str(contador), True, AZUL)
    pantalla.blit(Texto, [100, 100])

    pygame.display.flip()

    reloj.tick(1)
pygame.font.quit()
pygame.quit()