import pygame as pg
import random
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

         #start coordinates

        self.image = pg.transform.scale(pg.image.load(filename), (size, size))
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect(center = (x,y))
        self.start_x, self.start_y = self.rect.x,self.rect.y

    def update(self):
        direction_x,direction_y = 0,0
        if self.rect.x!=self.start_x:
            direction_x = 1 if self.start_x - self.rect.x > 0 else -1
        if self.rect.y!=self.start_y:
            direction_y = -1 if self.start_y - self.rect.y > 0 else 1
        self.rect.x+=direction_x
        self.rect.y-=direction_y
class Mouse_location(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.rel = (0,0)
        self.rect = pg.Rect(x,y,20,20)
        # self.rect = self.rect.centerx, self.rect.centery

# c1 = Circle(100,100,'circle.png',7)
circles = pg.sprite.Group()
for i in range(1500):
    circles.add(Circle(random.randint(100,400),random.randint(50,250),'circle.png',9))
x_mouse,y_mouse = pg.mouse.get_pos()
mouse_sprite = Mouse_location(x_mouse, y_mouse)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        elif event.type == pg.MOUSEMOTION:
            mouse_sprite.rect.centerx,mouse_sprite.rect.centery = pg.mouse.get_pos()
            mouse_sprite.rel = pg.mouse.get_rel()
        for s in circles:
            if pg.sprite.collide_rect(s,mouse_sprite):
                s.rect.x += mouse_sprite.rel[0]*2
                s.rect.y += mouse_sprite.rel[1]*2
    
    screen.fill((0,0,0))
    circles.update()
    circles.draw(screen)
    # screen.blit(c1.image,c1.rect)



    clock.tick(60)
    pg.display.update()