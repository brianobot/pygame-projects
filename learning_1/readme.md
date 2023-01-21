# Pygame Introduction.

# Process Description
- Pygame has a display surface, which is an image that is visible on the screen.
- the image is made up of pixels
- the main way of moving this pixel is by calling blits
  - blit copies pixel from one image to another
  - when you blit an image, you are basically changing the color of a pixel already on the screen
  - therefore blitting makes a copy of an image in a new position
  - erasing the previous image and redisplaying the screen causes an illusion of animation or movement

## Surfaces
Think of the surface as a blank peice of paper;
- you cab fill parts it with colors
- draw on it
- copy from and to it
- it can be any size and you can have as many surface as needed in a single program
- Note: one surface is special, the one gotten by running pygame.diaply.set_mode function
    it represent the screen of the user display

### How to create surfaces
- `pygame.display.set_mode(size)` # create the special screen surface
- `pygame.image.load(file)` # create a surface containing in an image
- `pygame.font.Font.render()` # create a surface that contains text
- `pygame.Surface` # create a surface that contains nothing at all

- Note: Always use the surface convert method on surface objects to ensure same pixel formats across your program
  ![Read here](https://www.pygame.org/docs/tut/newbieguide.html#use-surface-convert) for more details

## Things to Note about Pygame
- increased comfort with using python helps improve learning curve for game development
- always convert surface objects as noted in the how to create surfaces section about
- you not always need to use a sprite ti build game objects
  - Sprites and Groups are actually wrappers rounf the Surface and Rect object
- Do not worry about pixel perfect collision detection


## Rect
A Rect is simply a rectange that is defined by its top left corner position and its width and height
they can be defined as follows
- `rect = pygame.Rect(10, 10, 10, 10)`
- `rect = pygame.Rect((10, 10, 10, 10))`
- `rect = pygame.Rect((10, 10), (10, 10))`
- `rect = (10, 10, 10, 10)`
- `rect = ((10, 10, 10, 10))`