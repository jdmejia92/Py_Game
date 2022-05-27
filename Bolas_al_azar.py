import pygame as pg
import random as rd
pg.init()

FPS = 60
White = (255, 255, 255)
Rojo = (255, 0, 0)
Negro = (0, 0, 0)

class Bola():
    def __init__(self, padre, x, y, color = White, radio = 10):
        self.padre = padre

        self.x = x
        self.y = y
        self.color = color
        self.radio = radio
        self.vx = 0.1
        self.vy = 0.1

    def mover(self):
        self.x += self.vx 
        self.y += self.vy

        if self.x <= self.radio or self.x >= self.padre.get_width() - self.radio:
            self.vx *= -1

        if self.y <= self.radio or self.y >= self.padre.get_height() - self.radio:
            self.vy *= -1
        
    def dibujar(self):
        pg.draw.circle(self.padre, self.color, (self.x, self.y), self.radio)

class Game():
    
    def __init__(self, ancho=400, alto=600):
        self.pantalla = pg.display.set_mode((ancho, alto))
        pg.display.set_caption("Bolas al azar")
        #Creando dos instancias de la clase bola por separado
        '''self.bola = Bola(self.pantalla, ancho // 2, ancho // 2)
        self.bola1 = Bola(self.pantalla, 320, 520, radio=60)'''
        
        self.reloj = pg.time.Clock()
        
        #creacioon de lista de bolas con velocidades, direcciones y colores al azar
        self.bolas = []
        for i in range(rd.randrange(5, 20)):
            alt_radio = rd.randint(10, 30)
            nueva_bola = Bola(self.pantalla, rd.randrange(alt_radio, ancho - alt_radio),
                                rd.randrange(alt_radio, alto - alt_radio),  
                                (rd.randint(0, 255), rd.randint(0,255), rd.randint(0, 255)), alt_radio)
            nueva_bola.vx = rd.uniform(-6, 6)
            nueva_bola.vy = rd.uniform(-6, 6)
            self.bolas.append(nueva_bola)

        #Velocidades de las instanacias de la clase bola comentadas
        '''self.bola1.vx = 0.1
        self.bola1.vy = 0.1'''

    def bucle_ppal(self):
        game_over = False

        while not game_over:

            self.reloj.tick(FPS)

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True
            

            self.pantalla.fill(Negro)

            #mover y dibujas todas las instancias dentro de la lista self.bolas
            for nueva_bola in self.bolas:
                nueva_bola.mover()
                nueva_bola.dibujar()
            
            #Para mover y dibujar las bolas por separado
            '''self.bola.mover()
            self.bola1.mover()''' 
            '''self.bola.dibujar()
            self.bola1.dibujar()'''
            
            pg.display.flip()

if __name__ == '__main__':
    pg.init()

    game = Game()
    game.bucle_ppal()

    pg.quit()