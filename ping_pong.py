from pygame import *

class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[K_DOWN] and self.rect.y<window_height-80:
            self.rect.y+=self.speed
    def update_r(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[K_s] and self.rect.y<window_height-80:
            self.rect.y+=self.speed

back=(200,255,255)
win_width=600
win_height=500
window=display.set_mode((win_width,win_height))
window.fill(back)

game=True
finish=False
clock=time.Clock()
FPS=60



while game:
    for e in event.get():
        if e.type == QUIT:
            game=False
    if finish!=True:
        window.fill(back)
    display.update()
    clock.tick(FPS)