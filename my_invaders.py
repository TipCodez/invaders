import pygame, sys, random


from game import Game
pygame.init()


SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('space invader')

clock = pygame.time.Clock()
GREY = (29, 29, 27)

# creating a spaceship object
game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
# spaceship = Spaceship(SCREEN_WIDTH, SCREEN_HEIGHT)
# spaceship_group = pygame.sprite.GroupSingle()
# spaceship_group.add(spaceship)
# obstacle = Obstacle(100, 100)
# obstacle_sprite_group = pygame.sprite.Group
# obstacle_sprite_group.add(obstacle)

# # creating a laser object
# laser = Laser((100, 100), 6, SCREEN_HEIGHT)
# laser_group.add(laser, laser2)
# laser2 = Laser((200, 200), -6, SCREEN_HEIGHT)
# laser_group = pygame.sprite.Group()
SHOOT_LASER = pygame.USEREVENT
pygame.time.set_timer(SHOOT_LASER, 300)
MYSTERY_SHIP = pygame.USEREVENT + 1
pygame.time.set_timer(MYSTERY_SHIP, random.randint(4000, 8000))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SHOOT_LASER:
            game.alien_shoot()
        if event.type == MYSTERY_SHIP:
            game.create_mystery_ship()
            pygame.time.set_timer(MYSTERY_SHIP, random.randint(4000, 8000))


    #  updating
    # spaceship_group.update()
    game.spaceship_group.update()
    game.move_aliens()
    game.alien_lasers_group.update()
    game.mystery_ship_group.update()


    # Drawing
    screen.fill(GREY)
    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.laser_group.draw(screen)
    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(screen)
    game.aliens_group.draw(screen)
    game.alien_lasers_group.draw(screen)
    game.mystery_ship_group.draw(screen)
    pygame.display.update()
    clock.tick(60)
