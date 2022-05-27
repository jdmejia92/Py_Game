import pygame as pg
import sys

pg.init()

ancho = 600
largo = 800

pantalla = pg.display.set_mode((ancho, largo))

game_over = False

x = 300
y = 400

velocidad_x = 0.5
velocidad_y = 0.5

radio = 10

while not game_over:
    # Primero procesar eventos
    eventos = pg.event.get()
    for evento in eventos:
        if evento.type == pg.QUIT:
            game_over = True
        if evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE:
            pg.quit()
            sys.exit()

    # Modificar los objetos del juego
    x += velocidad_x
    y += velocidad_y

    if x >= ancho - radio or x <= radio:
        velocidad_x *= -1
    if y >= largo - radio or y <= radio:
        velocidad_y *= -1

    #Colocar color a la pantalla
    pantalla.fill((255, 0, 0))
    # Dibujar la bola
    bola = pg.draw.circle(pantalla, (255, 255, 0), (x, y), radio)

    # Refrescar la pantalla
    pg.display.flip()

pg.quit()