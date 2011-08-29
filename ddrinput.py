import pygame
JOY_EVENT = 7
KEY_EVENT = 2
X = 0
Y = 1
(LEFT, RIGHT, UP, DOWN, DROP) = range(5) 
KEY_LEFT = 276
KEY_UP = 273
KEY_DOWN = 274
KEY_RIGHT = 275
KEY_A = 97
KEY_S = 115
KEY_D = 100
KEY_W = 119
KEY_SPACE = 32
KEY_ESC = 27

DIRECTIONS = {0:'LEFT', 1:'RIGHT',  2:'UP', 3:'DOWN', 5:'DROP'}
class DdrInput(object):
  """
  DdrInput is a class to get input from the particular DDR pads and adapters we have.  It is not
  general or cross platform.  It uses pygame.  For something more general, use pad.py in the pydance
  library.  The pydance library doesn't work with our adapter, so we had to write our own code.  A
  few lines of code here are borrowed from the pydance library.


  DEBUG MODE:
    Use the arrow keys.  Hold down a modifier (alt, control, etc.) to get player 2
  """
  def __init__(self, debug_mode=True):
    """
    Debug mode prints inputs from the ddr pads and also enables the keyboard as an input
    """
    pygame.init() #safe to call multiple times
    self.init_joysticks()
    #This is just so that we can get key presses in the demo.  remove when we plug it into a ui
    screen = pygame.display.set_mode((640, 480))
    self.debug_mode = debug_mode

  def init_joysticks(self):
    pygame.joystick.init()
    try: totaljoy = pygame.joystick.get_count()
    except: totaljoy = 0
    print totaljoy, 'joysticks loaded'
    for i in range(totaljoy):
      m = pygame.joystick.Joystick(i)
      m.init()
  
  def poll(self):
    """
    Returns a tuple of player index (0 or 1) and move, 
    LEFT, RIGHT, UP, DOWN.  Returns None if there is no new input.  Only returns 1 input at a time.
    """
    event = pygame.event.poll()
    player_move = None
    if event.type == JOY_EVENT:
      player_index = event.joy
      #there may be a tricky quick way to code this, but this is more readable
      #value == 0 -> released
      if event.axis == X:
        if event.value < 0:
          player_move = LEFT
        elif event.value > 0:
          player_move = RIGHT
      else:
        if event.value > 0:
          player_move = DOWN
        elif event.value < 0:
          player_move = UP
      if self.debug_mode and player_move != None:
        print (player_index, player_move)
      if player_move != None:
        return (player_index, player_move)
      else:
        return None
    if self.debug_mode:
      if event.type == KEY_EVENT:
        if event.key == KEY_LEFT:
          player_index = 1
          player_move = LEFT
        elif event.key == KEY_RIGHT:
          player_index = 1
          player_move = RIGHT
        elif event.key == KEY_DOWN:
          player_index = 1
          player_move = DOWN
        elif event.key == KEY_UP:
          player_index = 1
          player_move = UP
        elif event.key == KEY_A:
          player_index = 0
          player_move = LEFT
        elif event.key == KEY_D:
          player_index = 0
          player_move = RIGHT
        elif event.key == KEY_S:
          player_index = 0
          player_move = DOWN
        elif event.key == KEY_W:
          player_index = 0
          player_move = UP
        elif event.key == KEY_ESC:
          player_index = 2
          player_move = "DIE"
        elif event.key == KEY_SPACE:
          player_index = 1
          player_move = "DROP"
       
        if player_move != None:
          return (player_index, player_move)
        else:
          return None
