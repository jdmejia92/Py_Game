import pygame as pg
import random as rd
import sys

#Establecer la cantidad de frames por segundo
FPS = 60

pg.init()

class Vigneta:
    def __init__(self, padre, x, y, ancho, alto, color = (255, 255, 255)):
        self.padre = padre
        self.x = x
        self.y = y
        self.color = color
        self.ancho = ancho
        self.alto = alto
        self.vx = 0
        self.vy = 0

    def dibujar(self):
        pass

    def mover(self):
        pass

class Ladrillo(Vigneta):
    def dibujar(self):
        pg.draw.rect(self.padre, self.color, (self.x, self.y, self.ancho, self.alto))

    def comprobarToque(self, bola):
        #hago cosas al tocar la bola
        pass

class Raqueta(Vigneta):
    def __init__(self, padre, x, y, ancho, alto, color = (255, 255, 0)):
        super().__init__(padre, x, y, ancho, alto, color)
        self.vx = 5

    def dibujar(self):
        pg.draw.rect(self.padre, self.color, (self.x, self.y, self.ancho, self.alto))

    def mover(self):
        teclas = pg.key.get_pressed()
        if teclas[pg.K_LEFT]:
            self.x -= self.vx
        if teclas[pg.K_RIGHT]:
            self.x += self.vx

        if self.x <= 0:
            self.x = 0
        if self.x + self.ancho >= self.padre.get_width():
            self.x = self.padre.get_width() - self.ancho

class Bola:
    def __init__(self, padre, x, y, color = (255, 255, 255), radio = 10):
        self.padre = padre
        self.x = x
        self.y = y
        self.color = color
        self.radio = radio
        #Lista con velocidades al azar
        self.velocity = [-5, 5]
        #Seleccion de velocidades al azar
        self.vx = rd.choice(self.velocity)
        self.vy = rd.choice(self.velocity)

    def mover(self):
        self.x += self.vx 
        self.y += self.vy

        if self.x <= self.radio or self.x >= self.padre.get_width() - self.radio:
            self.vx *= -1

        if self.y <= self.radio or self.y >= self.padre.get_height() - self.radio:
            self.vy *= -1
        
    def dibujar(self):
        pg.draw.circle(self.padre, self.color, (self.x, self.y), self.radio)

    #Funcion para comprobar si la bola choca con la raqueta, sin usar sprites
    def compruebaChoque(self, otro):
        if (self.x - self.radio in range(otro.x, otro.x + otro.ancho) or \
            self.x + self.radio in range(otro.x, otro.x + otro.ancho)) and \
            (self.y - self.radio in range(otro.y, otro.y + otro.alto) or \
            self.y + self.radio in range(otro.y, otro.y + otro.alto)):

            self.vy *= -1

class Game(): 
    def __init__(self, ancho=400, alto=600):
        self.pantalla = pg.display.set_mode((ancho, alto))
        pg.display.set_caption("Bolas al azar")
        self.bola = Bola(self.pantalla, ancho // 2, ancho // 2)
        self.raqueta = Raqueta(self.pantalla, ancho//2, alto - 30, 100, 20)

        self.reloj = pg.time.Clock()

    def bucle_ppal(self):
        game_over = False

        while not game_over:
            self.reloj.tick(FPS)
            
            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True
                if evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
            
            self.pantalla.fill((255, 0, 0))

            self.bola.mover()
            self.raqueta.mover()
            self.bola.compruebaChoque(self.raqueta)
            self.bola.dibujar()
            self.raqueta.dibujar()

            pg.display.flip()

if __name__ == '__main__':
    pg.init()

    game = Game()
    game.bucle_ppal()

    pg.quit()