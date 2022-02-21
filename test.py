from pickle import TRUE
from re import X
import pygame as pg
import random as rd
pg.init()

class Bola():
    def __init__(self, x, y, padre,  color = (255, 255, 255), radio = 10):
        self.x = x
        self.y = y
        self.color = color
        self.radio = radio
        self.vx = 0.1
        self.vy = 0.1
        self.padre = padre

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
        self.bola = Bola(ancho // 2, ancho // 2, self.pantalla)
        self.bola1 = Bola(320, 520, self.pantalla, radio=60)
        self.bolas = []
        aleatorio_color = (rd.randrange(0, 257), rd.randrange(0, 257), rd.randrange(0, 257))
        aleatorio_radio = rd.randint(10, 50)
        aleatorio_x = rd.randint(aleatorio_radio, ancho - aleatorio_radio)
        aleatorio_y = rd.randint(aleatorio_radio, alto - aleatorio_radio)
        
        for _ in range(rd.randrange(10, 20)):
            nueva_bola = Bola(aleatorio_x, aleatorio_y, self.pantalla, aleatorio_color, aleatorio_radio)
            self.bolas.append(nueva_bola)

        self.bola1.vx = 1
        self.bola1.vy = 1
                            
    def bucle_ppal(self):
        game_over = False

        while not game_over:

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True
            
            '''for bola in self.bolas:
                bola.Bola.mover()'''
            #self.bola.mover()
            #self.bola1.mover()
            self.pantalla.fill((255, 0, 0))    
            #dibujar todas las bolas
            #self.bola.dibujar()
            #self.bola1.dibujar()
            
            pg.display.flip()

if __name__ == '__main__':
    pg.init()

    game = Game()
    game.bucle_ppal()

    pg.quit()