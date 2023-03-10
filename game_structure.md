# Generic Game Structure

## Main Game File Structure
- **Load modules** which are required in the game. Standard stuff, except that you should remember to import the pygame local names as well as the pygame module itself

- **Resource handling classes**; define some classes to handle your most basic resources, which will be loading images and sounds, as well as connecting and disconnecting to and from networks, loading save game files, and any other resources you might have.

- **Game object classes**; define the classes for your game object. In the pong example, these will be one for the player's bat (which you can initialise multiple times, one for each player in the game), and one for the ball (which can again have multiple instances). If you're going to have a nice in-game menu, it's also a good idea to make a menu class.

**- Any other game functions**; define other necessary functions, such as scoreboards, menu handling, etc. Any code that you could put into the main game logic, but that would make understanding said logic harder, should be put into its own function. So as plotting a scoreboard isn't game logic, it should be moved into a function.

- **Initialise the game**, including the pygame objects themselves, the background, the game objects (initialising instances of the classes) and any other little bits of code you might want to add in.

- **The main loop**, into which you put any input handling (i.e. watching for users hitting keys/mouse buttons), the code for updating the game objects, and finally for updating the screen.

## Possible Modules for Larger Game Programs
- **objects.py**: store classes for game objects
- **resources.py**: store classes and code for managing game resources