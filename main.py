import pygame as pg
# from pygame.sprite import 


pg.init()



screen = pg.display.set_mode((500,300))
pg.display.set_caption('System')


class Circle(pg.sprite.Sprite):
    def __init__(self, x,y, filename, size):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pg.transform.scale(pg.image.load(filename), (size, size))
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect(center = (x,y))

c1 = Circle(100,100,'circle.png',7)

        

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.blit(c1.image,c1.rect)
    pg.display.update()