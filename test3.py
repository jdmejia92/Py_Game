from pickle import TRUE
from re import X
import pygame as pg
import random as rd
pg.init()


class Bola():
    def __init__(self, padre, x, y, cantidad, color = (255, 255, 255), radio = 10):
        self.padre = padre
        self.x = x
        self.y = y
        self.cantidad = cantidad
        self.color = color
        self.radio = radio
        self.vx = 0.1
        self.vy = 0.1

        self.radio = rd.randint(10, 50)
        self.x = rd.randint(self.radio, self.padre.get_width() - self.radio)
        self.y = rd.randint(self.radio, self.padre.get_height() - self.radio)
        self.color = (rd.randint(0, 255), rd.randint(0,255), rd.randint(0, 255))
                
    def mover(self):
        self.x += self.vx 
        self.y += self.vy

        if self.x <= self.radio or self.x >= self.padre.get_width() - self.radio:
            self.vx *= -1

    #self.radio >= self.x >= limDer - self.radio:

        if self.y <= self.radio or self.y >= self.padre.get_height() - self.radio:
            self.vy *= -1
        
    def dibujar(self):
        pg.draw.circle(self.padre, self.color, (self.x, self.y), self.radio)

class Game():
    
    def __init__(self, ancho=400, alto=600):
        self.pantalla = pg.display.set_mode((ancho, alto))
        pg.display.set_caption("Bolas al azar")
        self.bola = Bola(self.pantalla, ancho // 2, ancho // 2, 0)
        self.bola1 = Bola(self.pantalla, 320, 520, 0, radio=60)
        self.bolas = []
        alt_radio = rd.randint(10, 50)
        alt_x = rd.randrange(alt_radio, self.pantalla.get_width() - alt_radio)
        alt_y = rd.randrange(alt_radio, self.pantalla.get_height() - alt_radio)
        alt_color = (rd.randint(0, 255), rd.randint(0,255), rd.randint(0, 255))
        cantidad_bolas = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)   

        for i in range(rd.randrange(5, 10)):
            nueva_bola = Bola(self.pantalla, alt_x, alt_y, cantidad_bolas[i], alt_color, alt_radio)
            self.bolas.append(nueva_bola)

        self.bola1.vx = 0.1
        self.bola1.vy = 0.1

        #for velocidad
                            
    def bucle_ppal(self):
        game_over = False

        while not game_over:

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True
            
            for avanzaBola in self.bolas:
                avanzaBola.mover()
            self.bola.mover()
            self.bola1.mover()
            self.pantalla.fill((189, 236, 182))    
            #dibujar todas las bolas
            for dibujaBola in self.bolas:
                dibujaBola.dibujar()
            self.bola.dibujar()
            self.bola1.dibujar()
            
            pg.display.flip()

if __name__ == '__main__':
    pg.init()

    game = Game()
    game.bucle_ppal()

    pg.quit()