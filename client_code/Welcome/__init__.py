from ._anvil_designer import WelcomeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables



class Welcome(WelcomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.text_to_display = """Welcome, Agents! We need your help to save the Minecraft world.

A robber has stolen the kingdom's all powerful Netherite Sword. This sword has been enchanted to hide the identity of those who hold it. We need to find as much information about the robber as possible before the swords enchantment hides it.

There a 5 important locations to look at. The garden, vault, armor shop, potion shop, and the library. Watch out, as you engage with more people, the enchantment will become stronger and information will be harder and harder to get.

Press "Start Mission" to begin!"""
    # Counter for the position of next character to display
    self.current_position = 0
    # Start the typing effect
    anvil.js.call_js('startTypingEffect', self.type_text)



  def type_text(self):
    # Remove cursor if it's there
    if self.label_1.text.endswith('▮'):
      self.label_1.text = self.label_1.text[:-1]

    if self.current_position < len(self.text_to_display):
      # Append next character to label's text
      self.label_1.text += self.text_to_display[self.current_position]
      self.current_position += 1
      # Add cursor
      self.label_1.text += '▮'
    else:
      # Stop the typing effect
      self.text_box_1.visible = True
      anvil.js.call_js('stopTypingEffect')
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    open_form('GameScreen')


