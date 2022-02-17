from xmlrpc.client import boolean
import pygame as pg

pg.init()

ancho = 600
largo = 800

pantalla = pg.display.set_mode((ancho, largo))

game_over = False

x = 300
y = 400

velocidad_x = 1
velocidad_y = 1

radio = 10

while not game_over:
    # Primero procesar eventos
    eventos = pg.event.get()
    for evento in eventos:
        if evento.type == pg.QUIT:
            game_over = True

    # Modificar los objetos del juego
    x += velocidad_x
    y += velocidad_y

    if x >= ancho - radio or x <= radio:
        velocidad_x *= -1
    if y >= largo - radio or y <= radio:
        velocidad_y *= -1

    # Aqui no hay nada que hacer

    # Refrescar la pantalla
    pantalla.fill((255, 0, 0))
    bola = pg.draw.circle(pantalla, (255, 255, 0), (x, y), radio)

    pg.display.flip()

pg.quit()