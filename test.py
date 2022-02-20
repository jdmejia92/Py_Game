from pickle import TRUE
import pygame as pg
import random as rd
pg.init()

class Bola():
    def __init__(self, padre: pg.Surface):
        self.radio = rd.randint(10, 30) 
        self.x = rd.randrange(self.radio, padre.get_width()-self.radio)
        self.y = rd.randrange(self.radio, padre.get_height()-self.radio)
        self.color = (rd.randint(0, 255), rd.randint(0,255), rd.randint(0,255))
        self.vx = rd.uniform(0.1, 0.5)
        self.vy = rd.uniform(0.1, 0.5)
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
    bolas = []
    __color = (rd.randint(0, 255), rd.randint(0,255), rd.randint(0,255))
   
    def __init__(self, ancho=400, alto=600):
        self.pantalla = pg.display.set_mode((ancho, alto))
        pg.display.set_caption("Bolas al azar")
                     
        for i in range(4):
            self.LaBola = Bola(self.pantalla, self.__color[i])
            self.bolas.append(self.LaBola)
        
    def bucle_ppal(self):
        game_over = False

        while not game_over:

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True
            
            for i in self.bolas:
                self.LaBola.mover()
                self.pantalla.fill((245,245,220))
                self.LaBola.dibujar()
            
            for i in self.bolas:
                pg.draw.circle(self.pantalla, self.bola.color, (self.bola.x, self.bola.y), self.bola.radio)
            
            pg.display.flip()

if __name__ == '__main__':
    pg.init()

    game = Game()
    game.bucle_ppal()

    pg.quit()