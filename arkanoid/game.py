from pickle import TRUE
import pygame as pg
from arkanoid.escenas import Partida, GameOver

pg.init()

class Game:
    def __init__(self, ancho=600, alto=800):

        pantalla = pg.display.set_mode((ancho, alto))
        pg.display.set_caption("Arkanoid")
        self.escenas = [Partida(pantalla), GameOver(pantalla)]

    def lanzar(self):
        escena_activa = 0
        game_active = True
        while game_active:
            game_active = self.escenas[escena_activa].bucle_ppal()
            escena_activa += 1
            if escena_activa == len(self.escenas):
                escena_activa = 0