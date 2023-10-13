import pygame as pg
# from pygame.sprite import 


pg.init()


clock = pg.time.Clock()
screen = pg.display.set_mode((500,300))
pg.display.set_caption('System')


class Circle(pg.sprite.Sprite):
    def __init__(self, x,y, filename, size):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

        self.start_x, self.start_y = self.x,self.y #start coordinates

        self.image = pg.transform.scale(pg.image.load(filename), (size, size))
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect(center = (x,y))


class Mouse_location(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.rel = (0,0)
        self.rect = pg.Rect(x,y,1,1)

c1 = Circle(100,100,'circle.png',7)
x_mouse,y_mouse = pg.mouse.get_pos()
mouse_sprite = Mouse_location(x_mouse, y_mouse)
        

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        elif event.type == pg.MOUSEMOTION:
            mouse_sprite.x,mouse_sprite.y = pg.mouse.get_pos()
            mouse_sprite.rel = pg.mouse.get_rel()
            print(mouse_sprite.x, mouse_sprite.y)
    # print('False')
    # print(pg.mouse.get_pos(),pg.mouse.get_rel())
    screen.blit(c1.image,c1.rect)



    clock.tick(60)
    pg.display.update()