

import pygame
import random
from pygame.locals import *


ventana = {'ancho': 600, 'alto': 800}
COLOR_FUENTE = (250, 240, 40)
COLOR_FONDO = (13, 140, 255)
FPS = 40
enemigo = {'sizeMin': 10, 'sizeMax': 40, 'velocidadMin': 1, 'velocidadMax': 8}

TASANUEVOVILLANO = 6
TASAMOVIMIENTOJUGADOR = 5


def jugadorGolpeaVillano(rectanguloJugador, villano):
    for v in villanos:
        if rectanguloJugador.colliderect(v['rect']):
            return True
    return False


def dibujarTexto(texto, fuente, superficie, x, y):
    objetotexto = fuente.render(texto, 1, COLOR_FUENTE)
    rectangulotexto = objetotexto.get_rect()
    rectangulotexto.topleft = (x, y)
    superficie.blit(objetotexto, rectangulotexto)

def pantallaInicial(superficie):
    superficie.fill(COLOR_FONDO)
    fuente = pygame.font.SysFont('Dimitri Swank', 48)
    dibujarTexto('Evasor', fuente, superficie, (ventana['ancho'] / 2) - 80, (ventana['alto'] / 3))
    fuente = pygame.font.SysFont('Quesha', 46)
    dibujarTexto('Presione una tecla para comenzar.', fuente, superficie, (ventana['ancho'] / 2) - 220, (ventana['alto'] / 3) + 100)


def main():
    pygame.init()
    superficie = pygame.display.set_mode((ventana['ancho'], ventana['alto']))
    pygame.display.set_caption('Evasor')

    pygame.mixer.music.load('copycat.wav')
    #pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    imagenVillano = pygame.image.load('snake.png')

    trucoReversa = trucoLento = False
    contadorAgregarVillano = 0
    reloj = pygame.time.Clock()
    game_over = False
    juego_inicia = False
    pantallaInicial(superficie)
    villanos = []

    while not game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN and juego_inicia == False:
                juego_inicia = True
            #    pygame.mixer.music.play()
        if not trucoReversa and not trucoLento:
            contadorAgregarVillano += 1
        if contadorAgregarVillano == TASANUEVOVILLANO:
            contadorAgregarVillano = 0
            sizeEnemigo= random.randint(enemigo['sizeMin'], enemigo['sizeMax'])
            nuevoVillano = {'rect': pygame.Rect(random.randint(0, ventana['ancho'] - sizeEnemigo), 0 - sizeEnemigo, sizeEnemigo, sizeEnemigo), 'velocidad': random.randint(enemigo['velocidadMax'], enemigo['velocidadMax']), 'superficie':pygame.transform.scale(imagenVillano, (sizeEnemigo, sizeEnemigo))}
            villanos = [].append(nuevoVillano)
        if not juego_inicia:
            pantallaInicial(superficie)
        else:
            superficie.fill(COLOR_FONDO)
            for v in villanos:
                superficieVentana.blit(v['superficie'], v['rect'])
        pygame.display.flip()
        reloj.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()

'''
pygame.init()
superficieVentana = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA))
pygame.display.set_caption('Esquivador')
relojPrincipal = pygame.time.Clock()

pygame.mouse.set_visible(False)

fuente = pygame.font.SysFont(None, 48)

## SONIDOS **
sonidoJuegoTerminado = pygame.mixer.Sound('juegoterminado.wav')
pygame.mixer.music.load('Acrostics.wav')

imagenJugador = pygame.image.load('parrot.png')
rectanguloJugador = imagenJugador.get_rect()
imagenVillano = pygame.image.load('snake.png')

puntajeMax = 0
while True:
    # establece el comienzo del juego
    villanos = []
    puntaje = 0
    rectanguloJugador.topleft = (ANCHOVENTANA / 2, ALTOVENTANA - 50)
    moverIzquierda = moverDerecha = moverArriba = moverAbajo = False
    trucoReversa = trucoLento = False
    contadorAgregarVillano = 0
    pygame.mixer.music.play(-1, 0.0)

    while True: # el ciclo del juego se mantiene mientras se este jugando
        puntaje += 1 # incrementa el puntaje

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                terminar()

            if evento.type == pygame.KEYDOWN:
                if evento.key == ord('z'):
                    trucoReversa = True
                if evento.key == ord('x'):
                    trucoLento = True
                if evento.key == K_LEFT or evento.key == ord('a'):
                    moverDerecha = False
                    moverIzquierda = True
                if evento.key == K_RIGHT or evento.key == ord('d'):
                    moverIzquierda = False
                    moverDerecha = True
                if evento.key == K_UP or evento.key == ord('w'):
                    moverAbajo = False
                    moverArriba = True
                if evento.key == K_DOWN or evento.key == ord('s'):
                    moverArriba = False
                    moverAbajo = True

            if evento.type == KEYUP:
                if evento.key == ord('z'):
                    trucoReversa = False
                    puntaje = 0
                if evento.key == ord('x'):
                    trucoLento = False
                    puntaje = 0
                if evento.key == K_ESCAPE:
                        terminar()

                if evento.key == K_LEFT or evento.key == ord('a'):
                    moverIzquierda = False
                if evento.key == K_RIGHT or evento.key == ord('d'):
                    moverDerecha = False
                if evento.key == K_UP or evento.key == ord('w'):
                    moverArriba = False
                if evento.key == K_DOWN or evento.key == ord('s'):
                    moverAbajo = False

            if evento.type == MOUSEMOTION:
                # Si se mueve el ratón, este se mueve al lugar donde esté el cursor.
                rectanguloJugador.move_ip(evento.pos[0] - rectanguloJugador.centerx, evento.pos[1] - rectanguloJugador.centery)

        # Añade villanos en la parte superior de la pantalla, de ser necesarios.
        if not trucoReversa and not trucoLento:
            contadorAgregarVillano += 1
        if contadorAgregarVillano == TASANUEVOVILLANO:
            contadorAgregarVillano = 0
            tamañoVillano = random.randint(TAMAÑOMINVILLANO, SIZE_MAX_VILLANO)
            nuevoVillano = {'rect': pygame.Rect(random.randint(0, ANCHOVENTANA-tamañoVillano), 0 - tamañoVillano, tamañoVillano, tamañoVillano), 'velocidad': random.randint(VELOCIDADMINVILLANO, VELOCIDADMAXVILLANO),'superficie':pygame.transform.scale(imagenVillano, (tamañoVillano, tamañoVillano))}
            villanos = [].append(nuevoVillano)

        # Mueve el jugador.
        if moverIzquierda and rectanguloJugador.left > 0:
            rectanguloJugador.move_ip(-1 * TASAMOVIMIENTOJUGADOR, 0)
        if moverDerecha and rectanguloJugador.right < ANCHOVENTANA:
            rectanguloJugador.move_ip(TASAMOVIMIENTOJUGADOR, 0)
        if moverArriba and rectanguloJugador.top > 0:
            rectanguloJugador.move_ip(0, -1 * TASAMOVIMIENTOJUGADOR)
        if moverAbajo and rectanguloJugador.bottom < ALTOVENTANA:
            rectanguloJugador.move_ip(0, TASAMOVIMIENTOJUGADOR)

        # Mueve el cursor del ratón hacia el jugador.
        pygame.mouse.set_pos(rectanguloJugador.centerx, rectanguloJugador.centery)

        # Mueve los villanos hacia abajo.
        for v in villanos:
            if not trucoReversa and not trucoLento:
                v['rect'].move_ip(0, v['velocidad'])
            elif trucoReversa:
                v['rect'].move_ip(0, -5)
            elif trucoLento:
                v['rect'].move_ip(0, 1)

        # Elimina los villanos que han caido por debajo.
        for v in villanos[:]:
            if v['rect'].top > ALTOVENTANA:
                villanos.remove(v)

        # Dibuja el mundo del juego en la ventana.
        superficieVentana.fill(COLORFONDO)

        # Dibuja el puntaje y el puntaje máximo
        dibujarTexto('Puntaje: %s' % (puntaje), fuente, superficieVentana, 10, 0)
        dibujarTexto('Puntaje Máximo: %s' % (puntajeMax), fuente, superficieVentana, 10, 40)

        # Dibuja el rectángulo del jugador
        superficieVentana.blit(imagenJugador, rectanguloJugador)

        # Dibuja cada villano
        for v in villanos:
            superficieVentana.blit(v['superficie'], v['rect'])

        pygame.display.update()

        # Verifica si algún villano impactó en el jugador.
        if jugadorGolpeaVillano(rectanguloJugador, villanos):
            if puntaje > puntajeMax:
                puntajeMax = puntaje # Establece nuevo puntaje máximo
            break

        relojPrincipal.tick(FPS)

    # Detiene el juego y muestra "Juego Terminado"
    pygame.mixer.music.stop()
    sonidoJuegoTerminado.play()

    dibujarTexto('Juego Terminado', fuente, superficieVentana, (ANCHOVENTANA / 3)-40, (ALTOVENTANA / 3))
    dibujarTexto('Presione una tecla jugar de nuevo.', fuente, superficieVentana, (ANCHOVENTANA / 3) - 150, (ALTOVENTANA / 3) + 50)
    pygame.display.update()
    esperarTeclaJugador()

    #sonidoJuegoTerminado.stop()
'''

'''
https://www.gamedeveloperstudio.com/ - Game Developer Studio
https://freesound.org -level failed
https://opengameart.org/content/copycat syncopika
'''
