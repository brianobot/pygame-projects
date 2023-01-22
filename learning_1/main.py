import sys
import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def main():
    # Neccessary to ensure modules are initialized properly
    # Initialise screen
    pygame.init()

    size = width, height = (520, 440)
    screen = pygame.display.set_mode(size, pygame.SCALED) # set the window size
    pygame.display.set_caption('Test Game') # set the window title
    pygame.mouse.set_visible(False) # set the cursor within the window to invisible

    clock = pygame.time.Clock()

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    while True:
        # Process player inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        # Do logical updates here.
        # ...

        screen.fill("black")  # Fill the display with a solid color

        # Render the graphics here.
        # ...

        pygame.display.flip()  # Refresh on-screen display
        clock.tick(60)         # wait until next frame (at 60 FPS)
                

if __name__ == "__main__":
    main()