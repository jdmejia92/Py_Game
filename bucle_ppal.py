import pygame as pg

pg.init()

pantalla = pg.display.set_mode((600, 800))

game_over = False

while not game_over:
    # Primero procesar eventos
    eventos = pg.event.get()
    for evento in eventos:
        if evento.type == pg.QUIT:
            game_over = True

    # Modificar los objetos del juego
    # Aqui no hay nada que hacer

    # Refrescar la pantalla
    pantalla.fill((255, 0, 0))

    pg.display.flip()

pg.quit()