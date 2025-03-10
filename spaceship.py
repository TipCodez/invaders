import pygame

from  laser import  Laser

pygame.init()


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load("Graphics/spaceship.png")
        self.rect = self.image.get_rect(midbottom=(self.screen_width / 2, self.screen_height))
        self.speed = 6
        # creating laser groups
        self.laser_group = pygame.sprite.Group()
        self.laser_ready = True
        self.laser_time = 0
        self.laser_delay = 150


    def get_user_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_SPACE] and self.laser_ready:

            self.laser_ready = False
            laser = Laser(self.rect.center,5, self.screen_height)
            self.laser_group.add(laser)
            self.laser_time = pygame.time.get_ticks()
        # constraint movement

    def constraint_movement(self):
        if self.rect.right >= self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.left <= 0:
            self.rect.left = 0

    def recharge(self):
        if not self.laser_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_delay:
                self.laser_ready = True

    def update(self):
        self.get_user_input()
        self.constraint_movement()
        self.laser_group.update()
        self.recharge()
