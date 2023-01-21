import sys
import pygame

# Neccessary to ensure modules are initialized properly
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = width, height = (520, 440)
screen = pygame.display.set_mode(size, pygame.SCALED) # set the window size
pygame.display.set_caption('Test Game') # set the window title
pygame.mouse.set_visible(False) # set the cursor within the window to invisible

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(BLACK)

screen.blit(background, (0, 0))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
