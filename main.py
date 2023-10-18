import pygame as pg
import random
# from pygame.sprite import 


pg.init()


clock = pg.time.Clock()
screen = pg.display.set_mode((500,300))
pg.display.set_caption('System')
amount_screenshot = 0

class Circle(pg.sprite.Sprite):
    #Класс для спрайта круг
    def __init__(self, x,y, filename,filename2, size):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

         #start coordinates

        self.image = pg.transform.scale(pg.image.load(filename), (size, size))
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect(center = (x,y))
        self.start_x, self.start_y = self.rect.x,self.rect.y

        self.image2 = pg.transform.scale(pg.image.load(filename2), (size, size)) #Фиолетвый круг
        self.image2.set_colorkey(self.image2.get_at((0,0)))
        self.image1 = pg.transform.scale(pg.image.load(filename), (size, size))
        self.image1.set_colorkey(self.image.get_at((0,0)))
        # self.rect2 = self.image2.get_rect(center = (x,y))

    def update(self):
        #Функция возврата круга на исходную позицию
        direction_x,direction_y = 0,0
        
        # extra_x, extra_y = abs(self.start_x - self.rect.x), abs(self.start_y - self.rect.y)
        if self.rect.x!=self.start_x:
            self.image = self.image2
            # if extra_x>extra_y:
            #     direction_x = 2 if self.start_x - self.rect.x > 0 else -2
            # else:
            direction_x = 1 if self.start_x - self.rect.x > 0 else -1
        if self.rect.y!=self.start_y:
            self.image = self.image2
            # if extra_y>extra_x:
            #     direction_y = -2 if self.start_y - self.rect.y > 0 else 2
            # else:
            direction_y = -1 if self.start_y - self.rect.y > 0 else 1
    

        if self.rect.x == self.start_x and self.rect.y == self.start_y:
            direction_x,direction_y = 0,0
            self.image = self.image1
        self.rect.x+=direction_x
        self.rect.y-=direction_y
class Mouse_location(pg.sprite.Sprite):
    #Класс для объекта курсор мыши
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.rel = (0,0)
        self.rect = pg.Rect(x,y,20,20)


circles = pg.sprite.Group()
for i in range(1000):
    circles.add(Circle(random.randint(100,400),random.randint(50,250),'circle.png','circle2.png',9))
x_mouse,y_mouse = pg.mouse.get_pos()
mouse_sprite = Mouse_location(x_mouse, y_mouse)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        elif event.type == pg.MOUSEMOTION:
            #проверка движения мыши
            mouse_sprite.rect.centerx,mouse_sprite.rect.centery = pg.mouse.get_pos()
            mouse_sprite.rel = pg.mouse.get_rel()
        elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            #Скриншот состояния экрана
            rect = pg.Rect(0, 0, 500, 300)
            sub = screen.subsurface(rect)
            pg.image.save(sub, f"screenshot{amount_screenshot}.jpg")
            amount_screenshot+=1
        for s in circles:
            if pg.sprite.collide_rect(s,mouse_sprite):
                #проверка прикосновения спрайтов с мышкой
                s.rect.x += mouse_sprite.rel[0]*3 
                s.rect.y += mouse_sprite.rel[1]*3 

    
    screen.fill((0,0,0))
    circles.update()
    circles.draw(screen)
    # screen.blit(c1.image,c1.rect)



    clock.tick(60)
    pg.display.update()