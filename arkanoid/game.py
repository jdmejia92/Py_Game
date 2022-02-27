from pickle import TRUE
import pygame as pg
import random as rd
from arkanoid.entities import Bola, Raqueta, Ladrillo
from arkanoid import FPS, niveles

pg.init()

class Game():
    
    def __init__(self, ancho=600, alto=800):
        self.pantalla = pg.display.set_mode((ancho, alto))
        pg.display.set_caption("Bolas al azar")
        self.bola = Bola(self.pantalla, ancho // 2, ancho // 2)
        self.raqueta = Raqueta(self.pantalla, ancho//2, alto - 30, 100, 20)
        self.ladrillos = []
        self.todos = []
        self.todos.append(self.bola)
        self.todos.append(self.raqueta)
        self.contador_vidas = 3

        self.reloj = pg.time.Clock()

    def crea_ladrillos(self, nivel):
        for col, fil in niveles[nivel]:
            l = Ladrillo(self.pantalla, 5 + 60 * col, 25 + 30 * fil, 50, 20)
            self.ladrillos.append(l)

        self.todos += self.ladrillos
              
    def bucle_ppal(self):
        nivel = 0

        while self.contador_vidas > 0 and nivel < len(niveles):
            self.crea_ladrillos(nivel)

            while self.contador_vidas > 0 and len(self.ladrillos) > 0:
                   
                self.reloj.tick(FPS)
                
                eventos = pg.event.get()
                for evento in eventos:
                    if evento.type == pg.QUIT:
                        self.contador_vidas = 0
                            
                self.pantalla.fill((255, 0, 0))

                for objeto in self.todos:
                    objeto.mover()
                    
                self.bola.compruebaChoque(self.raqueta)

                if not self.bola.esta_viva:
                    self.contador_vidas -= 1
                    self.bola.reset()
                
                for objeto in self.todos:
                    objeto.dibujar()
                
                for ladrillo in self.ladrillos:
                    if self.bola.compruebaChoque(ladrillo):
                        self.ladrillos.remove(ladrillo)
                        self.todos.remove(ladrillo)

                    ladrillo.dibujar()
                                    
                pg.display.flip()

            nivel += 1
            self.bola.reset()