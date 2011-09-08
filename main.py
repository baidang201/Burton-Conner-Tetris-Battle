from time import sleep, time
import random
import sys
from renderer import *
from ddrinput import DdrInput
from ddrinput import DIRECTIONS
import pygame
import util
import figure_builder

LETTER_WIDTH = 6

class Animation:

  def __init__(self):
    self.gui = [PygameRenderer(), LedRenderer()]
    self.letters = self.create_letter_dict()
    self.base = {}
    self.animate()

  def sun(self):
    sun = self.get_letter_dict("sun","yellow")
    self.base = {}
    self.add_pic(self.base,sun,(2,0))

    self.display(self.base)
    sleep(1)
    for i in range(20):
      self.display(self.base)
      self.base = util.shift_dict(self.base, (0,1))
      sleep(.3)

  def moon(self):
    moon = self.get_letter_dict("moon","yellow")
    stars = self.get_letter_dict("stars","gray")
    self.base = {}
    self.add_pic(self.base,moon,(3,20))
    for i in range(20):
      print "here"
      self.display(self.base)
      self.base = util.shift_dict(self.base, (0,-1))
      sleep(.3)
    
    for i in range(30):
      the_moon = {}
      self.base = the_moon
      self.add_pic(the_moon,stars,(0,0))
      stars_on = random.sample(stars,30)
      for key in stars_on:
        self.base[key] = "white"
      self.add_pic(the_moon,moon,(3,0))
      self.display(self.base)
      sleep(.3)

  def scroll_text(self, text):
    word_dict = {}
    for letter in text:
      letter = self.get_letter_dict(letter, "white")
      word_dict = util.compose_dicts(word_dict, letter, (LETTER_WIDTH, 0))
    self.base = word_dict
    import pdb; pdb.set_trace()
    for i in range(50):
      self.display(self.base)
      self.base = util.shift_dict(self.base, (-1, 0))
      sleep(.3)

  def animate(self):
    self.scroll_text("GOODNIGHT ALLY")
    self.sun()
    self.moon()
  
  def display(self,d):
    [gui.render_game(d) for gui in self.gui]

  def create_letter_dict(self):
    d = {}
    d["moon"] = [(5,0),(6,0),(7,0),(8,0),(3,1),(4,1),(5,1),(6,1),
           (2,2),(3,2),(4,2),(1,3),(2,3),(3,3),(1,4),(2,4),(3,4),
           (0,5),(1,5),(2,5),(3,5),
           (5,10),(6,10),(7,10),(8,10),(3,9),(4,9),(5,9),(6,9),
           (2,8),(3,8),(4,8),(1,7),(2,7),(3,7),(1,6),(2,6),(3,6)]

    d["sun"] = self.make_sun()
    d["stars"] = self.make_stars()
    d[" "] = {}
    return d

  def make_stars(self):
    stars = []
    for i in range(40):
      stars += [(random.randint(0,19),random.randint(0,10))]
    return stars    
    
  def make_sun(self):
    final = []
    full = []
    half = []
    quad = [(0,0),(1,0),(2,0),(4,0),(5,0),(6,0),(0,1),(1,1),(2,1),
       (0,2),(1,2),(3,3),(4,3),(0,4),(4,4),(5,4),(0,5),(5,5),
       (0,6),(6,5),(6,6),(7,0),(0,7)]
    half = quad[:]
    for (x,y) in quad:
      half += [(-y-1,x)]
    full = half[:]
    for (x,y) in half:
      full += [(x,-y-1)]
    for (x,y) in full:
      final += [(x+8,y+8)]
    print final
    return final
    
    

  def create_picture_dict(self): #multi-color pics...
    d = {}
    

  def get_letter_dict(self,letter, color):
    if not letter in self.letters:
      letter = letter.lower()
      try:
        letter_array = figure_builder.dict_from_image_file('img/' + letter + '.png', (5,5)) 
      except IOError:
        return {}
    else:
      letter_array = self.letters[letter]
    d={}
    for key in letter_array:
      d[key] = color
    return d
    
  def add_pic(self,start_dict,new_pic,top_left):
    for (x,y) in new_pic:
      start_dict[x+top_left[0],y+top_left[1]]=new_pic[(x,y)]

class TextAnimation:
  def __init__(self, text):
    super(TextAnimation, self).__init__()
    self.base = {}
    text_width = 0
    for letter in text:
      letter_dict = get_dict(letter) ###replace
      util.compose_dicts(self.base, letter, LETTER_WIDTH)
      text_width += LETTER_WIDTH
  
    self.base = util.shift_dict(self.base, (-text_width, 0))
if __name__ == "__main__":
  animation = Animation()
