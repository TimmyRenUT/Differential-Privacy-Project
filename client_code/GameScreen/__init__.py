from anvil import *
import anvil
from anvil import URLMedia
from ._anvil_designer import GameScreenTemplate
from .ClueForm import ClueForm  # Import the single ClueForm for all clues

class GameScreen(GameScreenTemplate):
    def __init__(self, **properties):
        # Initialize the form
        self.init_components(**properties)
        url = server.get_app_origin()
        # URL for the labeled map image
        self.map_url = f"{url}/_/theme/labeled_map.png"

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
                "x": 450,
                "y": 170,
                "width": 250,
                "height": 250,
                "type": "text",
                "content": "The vault was trashed, and an enchanted Netherite sword is missing. The robber used a diamond tool to escape unseen."
            },
            "Garden": {
                "x": 50,
                "y": 680,
                "width": 550,
                "height": 270,
                "type": "image",
                "content": "garden.png"  # Replace with your asset name
            },
            "Potion Shop": {
                "x": 1080,
                "y": 500,
                "width": 200,
                "height": 150,
                "type": "text",
                "content": "Sophie spent all night brewing potions to save Ethan after his epic battle with a wither."
            },
            "Library": {
                "x": 600,
                "y": 480,
                "width": 200,
                "height": 150,
                "type": "text",
                "content": "Lucas spent all night comforting Gavin, who witnessed the robber rob the armorsmith and charge toward his garden."
            },
            "Armor Shop": {
                "x": 850,
                "y": 580,
                "width": 200,
                "height": 200,
                "type": "image",
                "content": "armor_shop.png"  # Replace with your asset name
            }
        }

        # Bind the mouse click event
        self.canvas_1.set_event_handler("mouse_down", self.canvas_mouse_down)

        # Set initial text for the noise level display
        self.update_noise_level_display()

    def timer_1_tick(self, **event_args):
        """This method is called every interval seconds."""
        print("Timer tick triggered.")  # Debugging
        self.timer_1.set_event_handler("tick", None)  # Stop the timer
        self.load_map()

    def load_map(self):
        """Load and scale the map image onto the canvas."""
        print("Attempting to load the map image...")  # Debugging
        image_media = URLMedia(self.map_url)

        if not image_media:
            print("Error: Failed to create URLMedia object.")
            return

        try:
            # Natural dimensions of the image
            img_width, img_height = 1419, 768
            canvas_width, canvas_height = self.canvas_1.width, self.canvas_1.height

            # Calculate scaling factors
            self.scale_x = canvas_width / img_width
            self.scale_y = canvas_height / img_height

            # Maintain aspect ratio
            if self.scale_x < self.scale_y:
                self.scale_y = self.scale_x
            else:
                self.scale_x = self.scale_y

            # Calculate draw position to center the image
            draw_width = img_width * self.scale_x
            draw_height = img_height * self.scale_y
            draw_x = (canvas_width - draw_width) / 2
            draw_y = (canvas_height - draw_height) / 2

            # Clear the canvas
            self.canvas_1.clear_rect(0, 0, canvas_width, canvas_height)

            # Draw the scaled image
            self.canvas_1.draw_image(image_media, draw_x, draw_y, draw_width, draw_height)
            print("Map loaded and drawn successfully.")
        except Exception as e:
            print(f"Error loading map: {e}")

    def update_noise_level_display(self):
        """
        Update the noise level label on the screen.
        """
        self.label_noise_level.text = f"Noise Level: {self.game_state['noise_level']}"

    def canvas_mouse_down(self, x, y, button, **event_args):
        """Handle mouse clicks on the canvas."""
        # Adjust click coordinates back to natural image scale
        scaled_x = x / self.scale_x
        scaled_y = y / self.scale_y

        print(f"Mouse clicked at ({scaled_x}, {scaled_y})")  # Debugging

        # Check which region was clicked
        for region_name, region_data in self.regions.items():
            if (
                region_data["x"] < scaled_x < region_data["x"] + region_data["width"]
                and region_data["y"] < scaled_y < region_data["y"] + region_data["height"]
            ):
                print(f"{region_name} clicked!")  # Debugging

                # Increment noise level
                self.game_state["noise_level"] += 1
                self.update_noise_level_display()

                # Open the ClueForm with the clicked region's data
                form = ClueForm(
                    region_name=region_name,
                    clue=region_data,
                    game_state=self.game_state
                )
                get_open_form().content_panel.clear()
                get_open_form().content_panel.add_component(form)
                return
