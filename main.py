import pygame
from logic import mainWindow
from utilities import clock, gameWin, groundHeight, height, width

pygame.init()
pygame.display.set_mode((900, 600))

from tank import tank

mainWindow()
