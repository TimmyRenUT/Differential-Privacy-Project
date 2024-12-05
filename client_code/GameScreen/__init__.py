from anvil import *
import anvil
from anvil import URLMedia
from ._anvil_designer import GameScreenTemplate
import json

class GameScreen(GameScreenTemplate):
    def __init__(self, **properties):
        # Initialize the form
        self.init_components(**properties)
        url = server.get_app_origin()
        # URL for the labeled map image
        self.map_url = f"{url}/_/theme/labeled_map.png"

        with open(anvil.server.fetch_file("precomputed_clues.json")) as f:
          self.precomputed_clues = json.load(f)

        # Canvas size
        self.canvas_1.width = 800
        self.canvas_1.height = 600

        # Initialize game state
        self.game_state = {
            "noise_level": 0,
            "crossed_out_suspects": [],
        }

        # Define clickable regions in one place
        self.regions = {
            "Vault": {
                "name": 'Vault',
                "x": 450,
                "y": 170,
                "width": 250,
                "height": 250,
                "type": "text",
                "content": "The vault was trashed, and an enchanted Netherite sword is missing. The robber used a diamond tool to escape unseen."
            },
            "Garden": {
                "name": 'Garden',
                "x": 50,
                "y": 680,
                "width": 550,
                "height": 270,
                "type": "image",
                "content": "garden.png"
            },
            "Potion Shop": {
                "name": 'Potion Shop',
                "x": 1080,
                "y": 500,
                "width": 200,
                "height": 150,
                "type": "text",
                "content": "Sophie spent all night brewing potions to save Ethan after his epic battle with a wither."
            },
            "Library": {
                "name": 'Library',
                "x": 600,
                "y": 480,
                "width": 200,
                "height": 150,
                "type": "text",
                "content": "Lucas spent all night comforting Gavin, who witnessed the robber rob the armorsmith and charge toward his garden."
            },
            "Armor Shop": {
                "name": 'Armor Shop',
                "x": 850,
                "y": 580,
                "width": 200,
                "height": 200,
                "type": "image",
                "content": "armory.png"
            }
        }

        # Bind the mouse click event
        self.canvas_1.set_event_handler("mouse_down", self.canvas_mouse_down)

        # Set initial text for the noise level display
        self.update_noise_level_display()

        # Hide clue components initially
        self.show_map()

    def timer_1_tick(self, **event_args):
        """
        Timer tick to handle the initial map loading.
        """
        print("Timer tick triggered.")  # Debugging
        self.timer_1.set_event_handler("tick", None)  # Disable the timer
        self.timer_1.enabled = False
        self.load_map()

    def show_map(self):
        """
        Show the map and hide clue components.
        """
        print("Showing map...")  # Debugging
        self.canvas_1.visible = True
        self.label_noise_level.visible = True
        self.button_back_to_map.visible = False
        self.canvas_1.clear_rect(0, 0, self.canvas_1.width, self.canvas_1.height)

        # Draw the map
        self.load_map()

    def show_clue(self, region_data):
        """
        Prepare to show the clue for the selected region.
        """
        print(f"Preparing to show clue for region: {region_data['name']}")  # Debugging

        # Hide the map components
        self.canvas_1.visible = True
        self.label_noise_level.visible = True
        self.button_back_to_map.visible = True

        # Store region data for use in the timer
        self.current_region = region_data

        # Reset the timer to delay clue rendering
        self.timer_1.set_event_handler("tick", self.load_clue_tick)
        self.timer_1.interval = 0.1
        self.timer_1.enabled = True

    def load_clue_tick(self, **event_args):
        """
        Timer tick to load the clue after a short delay.
        """
        print("Loading clue...")  # Debugging
        self.timer_1.enabled = False  # Disable the timer
        self.timer_1.set_event_handler("tick", None)  # Unset the timer event

        # Clear the canvas
        self.canvas_1.clear_rect(0, 0, self.canvas_1.width, self.canvas_1.height)

        # Render the clue based on type
        if self.current_region["type"] == "text":
            print("Rendering text clue...")  # Debugging
            self.display_clue_book(self.current_region["content"])
        elif self.current_region["type"] == "image":
            print("Rendering image clue...")  # Debugging
            self.display_clue_image(self.current_region["content"])
    
    def display_clue_book(self, region_name):
        """
        Display the text clue with a typing animation effect, using precomputed values.
        """
        # Get the current noise level
        noise_level = max(1, min(self.game_state["noise_level"], 10))  # Ensure noise level is within bounds
        
        # Fetch precomputed degraded text and l_list
        precomputed_data = self.precomputed_clues[region_name][str(noise_level)]
        degraded_text = precomputed_data["degraded_text"]
        l = precomputed_data["l_list"]
    
        # Book image setup
        book_image_url = f"{anvil.server.get_app_origin()}/_/theme/minecraft_book.png"
        canvas_width = self.canvas_1.width
        canvas_height = self.canvas_1.height
    
        book_width = canvas_width * 0.35
        book_height = canvas_height * 0.7
        book_x = (canvas_width - book_width) / 2
        book_y = (canvas_height - book_height) / 2 - 100
    
        try:
            # Render the book image
            image = anvil.URLMedia(book_image_url)
            self.canvas_1.clear_rect(0, 0, canvas_width, canvas_height)
            self.canvas_1.draw_image(image, book_x, book_y, book_width, book_height)
    
            # Typing effect setup
            self.canvas_1.fill_style = "#000000"
            self.canvas_1.font = "14px sans-serif"
            text_x = book_x + book_width * 0.1
            text_y = book_y + book_height * 0.2
            line_height = 20
            max_line_length = 30
    
            # Typing animation using the precomputed `l` list
            idx = 0
            for word in degraded_text.split():
                for char in word + " ":
                    for _ in range(l[idx] + 1):  # Use l[idx] to control typing attempts
                        output = random.choice(string.ascii_letters + " ")
                        self.canvas_1.clear_rect(text_x, text_y - line_height, canvas_width, line_height)
                        self.canvas_1.fill_text(output, text_x, text_y)
                        time.sleep(0.03)
                    self.canvas_1.clear_rect(text_x, text_y - line_height, canvas_width, line_height)
                    self.canvas_1.fill_text(char, text_x, text_y)  # Final correct character
                    text_x += self.canvas_1.measure_text(char).width
                    idx += 1
                    if text_x > canvas_width - 20:
                        text_x = book_x + book_width * 0.1
                        text_y += line_height
        except Exception as e:
            print(f"Error rendering typing effect: {e}")


    def display_clue_image(self, image_name):
        """
        Display an image-based clue, selecting the appropriate blur level based on the noise level.
        """
        # Determine the current noise level (clamp between 1 and 10 to match the assets)
        noise_level = max(1, min(self.game_state["noise_level"], 10))
        
        # Construct the image name based on the noise level
        image_file = image_name.replace(".png", f"_blurred_level_{noise_level}.png")
        image_url = f"{anvil.server.get_app_origin()}/_/theme/{image_file}"
        
        canvas_width = self.canvas_1.width
        canvas_height = self.canvas_1.height
    
        try:
            print(f"Loading clue image from {image_url}...")  # Debugging
            image = anvil.URLMedia(image_url)
            self.canvas_1.draw_image(image, 0, 0, canvas_width, canvas_height)
            print("Clue image rendered successfully.")  # Debugging
        except Exception as e:
            print(f"Error rendering clue image: {e}")
    

    def update_noise_level_display(self):
        """
        Update the noise level label on the screen.
        """
        self.label_noise_level.text = f"Noise Level: {self.game_state['noise_level']}"

    def canvas_mouse_down(self, x, y, button, **event_args):
        """Handle mouse clicks on the canvas."""
        scaled_x = x / self.scale_x
        scaled_y = y / self.scale_y
    
        for region_name, region_data in self.regions.items():
            if (
                region_data["x"] < scaled_x < region_data["x"] + region_data["width"]
                and region_data["y"] < scaled_y < region_data["y"] + region_data["height"]
            ):
                print(f"{region_name} clicked!")  # Debugging
                self.game_state["noise_level"] += 1
                self.update_noise_level_display()
                self.display_clue_book(region_name)  # Pass region name to display the clue
                return


    def button_back_to_map_click(self, **event_args):
        """
        Handle 'Back to Map' button click.
        """
        print("Returning to map...")  # Debugging
        self.canvas_1.visible = True
        self.button_back_to_map.visible = False
        # Reset the timer to delay map loading
        self.timer_1.set_event_handler("tick", self.reload_map_tick)
        self.timer_1.interval = 0.1
        self.timer_1.enabled = True
    
    def reload_map_tick(self, **event_args):
        """
        Timer tick to reload the map after returning from clue view.
        """
        print("Reloading map...")  # Debugging
        self.timer_1.enabled = False
        self.timer_1.set_event_handler("tick", None)
        self.show_map()
    
    def load_map(self):
        """Load and scale the map image onto the canvas."""
        print("Attempting to load the map image...")  # Debugging
        image_media = URLMedia(self.map_url)
    
        try:
            img_width, img_height = 1419, 768
            canvas_width = self.canvas_1.width
            canvas_height = self.canvas_1.height
    
            self.scale_x = canvas_width / img_width
            self.scale_y = canvas_height / img_height
    
            if self.scale_x < self.scale_y:
                self.scale_y = self.scale_x
            else:
                self.scale_x = self.scale_y
    
            draw_width = img_width * self.scale_x
            draw_height = img_height * self.scale_y
            draw_x = (canvas_width - draw_width) / 2
            draw_y = (canvas_height - draw_height) / 2
    
            self.canvas_1.clear_rect(0, 0, canvas_width, canvas_height)
            self.canvas_1.draw_image(image_media, draw_x, draw_y, draw_width, draw_height)
            print("Map loaded and drawn successfully.")
        except Exception as e:
            print(f"Error loading map: {e}")
