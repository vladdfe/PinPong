from pygame import *

back = (200, 255, 255)
win_width = 600
win_height
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60
class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        # Вызываем конструктор класса (Sprite):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (whight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
while game:
    for e in event.get():
        if e tipe = QUIT:
            game = False

    display.update()
    clock.tick(FPS)
