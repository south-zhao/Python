import pygame
import random

ENEMY_EVENT = pygame.USEREVENT
FIRE = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    '''描述游戏中元素的类'''

    def __init__(self, image_name, speed=1):
        super().__init__()

        self.image = pygame.image.load(image_name)
        # self.rect: 控制图片的那个矩形（图片所在的矩形）
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        self.rect.y += self.speed


class BackGound(GameSprite):
    '''背景图片类'''

    def __init__(self, image_name, alt=False):
        super().__init__(image_name)

        # 设置背景图片的起始位置 如果alt==True，就将这种背景图片放到屏幕的上方
        if alt:
            self.rect.bottom = 0

    # 背景图片如果飞出了屏幕的底部就要挪动到屏幕的顶部
    def update(self, *args):
        super().update()

        if self.rect.y >= 700:
            # self.rect.y = -700
            self.rect.bottom = 0


class Enemy(GameSprite):
    def __init__(self, image_name, speed=1):
        super().__init__(image_name, speed)
        # 敌机出现在屏幕的顶部
        self.rect.bottom = 0
        # 随机出现在屏幕的水平方向上（x坐标是随机）
        max = 480 - self.rect.width
        self.rect.x = random.randint(0, max)

    def update(self, *args):
        super().update()
        # 判断敌机是否冲出了屏幕
        if self.rect.y >= 700:
            self.kill()


class Bullet(GameSprite):
    def __init__(self, x, y, image_name, speed=2):
        super().__init__(image_name, speed)
        self.rect.centerx = x
        self.rect.bottom = y

    def update(self, *args):
        self.rect.y -= self.speed


class Hero(GameSprite):
    def __init__(self, image_name, speed=0):
        super().__init__(image_name, speed)

        self.rect.y = 700 - self.rect.height - 30
        self.rect.x = 240 - self.rect.width // 2

        self.bullet_group = pygame.sprite.Group()

    def update(self, *args):
        self.rect.x += self.speed
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= 480 - self.rect.width:
            self.rect.x = 480 - self.rect.width

    def fire(self):
        print("发射子弹")
        for x in range(3):
            b = Bullet(self.rect.centerx, self.rect.y - x * 20, "./images/bullet1.png")
            self.bullet_group.add(b)
