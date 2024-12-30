from ._anvil_designer import Form1Template
from anvil import *
import random
import string 
import time

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_fill.visible = True
    # Any code you write here will run before the form opens.
    self.characters = 'Congrats Ae!Yudicvhbw'
    s = 'Congrats Agent! You discovered the robber and saved the town!'
    self.l = []
    for i in s:
        random.seed(48)
        count = -1
        while True:
            output = random.choice(self.characters)
            count += 1
            if i == output:
                self.l.append(count)
                break
    
  def fill(self,l, **event_args):
    #print(l)
    for i in l:
      random.seed(48)
      sleep_time = 1/(i+550)
      for x in range(i+1):
        output = random.choice(self.characters)
        self.label_fill.text += output
        time.sleep(sleep_time)
        self.label_fill.text = self.label_fill.text[:-1]
      self.label_fill.text += output

  def timer_1_tick(self, **event_args):
    self.timer_1.set_event_handler("tick", None)  # Disable the timer
    self.timer_1.enabled = False
    self.fill(self.l)
