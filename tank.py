import pygame
from utilities import gameWin

tankWidth = 60
tankHeight = 60
turretWidth = 5
wheelWidth = 5

pygame.init()  # Initialize pygame.display here

tank_image = pygame.image.load("C:\\Users\\Oved Ramirez\\Desktop\\Pycharm\\FinalProject\\Project 2\\src\\tankicon.png").convert_alpha()
tank_image = pygame.transform.scale(tank_image, (tankWidth, tankHeight))

background_image = pygame.image.load("C:\\Users\\Oved Ramirez\\Desktop\\Pycharm\\FinalProject\\Project 2\\src\\background.jpg").convert_alpha()
ground_image = pygame.image.load("C:\\Users\\Oved Ramirez\\Desktop\\Pycharm\\FinalProject\\Project 2\\src\\brick.jpg").convert_alpha()
wall_image = pygame.image.load("C:\\Users\\Oved Ramirez\\Desktop\\Pycharm\\FinalProject\\Project 2\\src\\brick.jpg").convert_alpha()
wall_image = pygame.transform.scale(wall_image, (60, 400))

def tank(x, y, turPos, tank):
    # tank=1 if player's tank and -1 if computer's tank
    x = int(x)
    y = int(y)

    # Original tank dimensions
    original_tank_width = 60
    original_tank_height = 60

    # Scale factor for width and height
    width_scale = tankWidth / original_tank_width
    height_scale = tankHeight / original_tank_height

    # Adjusted coordinates based on scaling
    adjusted_x = x - (original_tank_width * width_scale / 2)
    adjusted_y = y - (original_tank_height * height_scale / 2)

    locs = [[27, 2], [26, 5], [25, 8], [23, 12], [20, 14], [18, 15], [15, 17], [13, 19], [11, 21], [9,23], [7,25]]
    possibleTurrets = []
    for i in locs:
        possibleTurrets.append((x - 1 * i[0], y - i[1]))

    tank_img = tank_image if tank == 1 else pygame.transform.flip(tank_image, True, False)
    tank_rect = tank_img.get_rect(center=(x, y))
    gameWin.blit(tank_img, tank_rect)

    return possibleTurrets[turPos]
