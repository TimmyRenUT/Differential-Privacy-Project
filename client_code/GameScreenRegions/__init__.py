from anvil import *
import anvil
from anvil import URLMedia
from ._anvil_designer import GameScreenRegionsTemplate
class GameScreenRegions(GameScreenRegionsTemplate):
    """
    Testing area for determining where the clickable regions are, not in the actual app
    """
    def __init__(self, **properties):
        # Initialize the form
        self.init_components(**properties)
        url = server.get_app_origin()
        # URL for the labeled map image
        self.map_url = f"{url}/_/theme/labeled_map.png"
      
        # Canvas size
        self.canvas_1.width = 800
        self.canvas_1.height = 600

        # Store scaling factors
        self.scale_x = 1
        self.scale_y = 1
        # Define clickable regions in one place
        self.regions = [
            {"name": "Vault", "x": 450, "y": 20, "width": 250, "height": 250, "color": "red"},
            {"name": "Garden", "x": 50, "y": 560, "width": 550, "height": 270, "color": "blue"},
            {"name": "Potion Shop", "x": 1080, "y": 380, "width": 200, "height": 150, "color": "green"},
            {"name": "Library", "x": 600, "y": 360, "width": 200, "height": 150, "color": "yellow"},
            {"name": "Armor Shop", "x": 850, "y": 460, "width": 200, "height": 200, "color": "purple"}
        ]

        # Bind the mouse click event
        self.canvas_1.set_event_handler("mouse_down", self.canvas_mouse_down)

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
            draw_y = (canvas_height - draw_height) / 2 - 75

            # Clear the canvas
            self.canvas_1.clear_rect(0, 0, canvas_width, canvas_height)

            # Draw the scaled image
            self.canvas_1.draw_image(image_media, draw_x, draw_y, draw_width, draw_height)
            print("Map loaded and drawn successfully.")
        except Exception as e:
            print(f"Error loading map: {e}")

        # Draw regions for visualization
        self.draw_regions()

    def draw_regions(self):
        """Draw rectangles for clickable regions, scaled to fit the image."""
        print("Drawing clickable regions...")  # Debugging
        for region in self.regions:
            self.draw_scaled_rect(region)

    def draw_scaled_rect(self, region):
        """Draw a scaled rectangle."""
        self.canvas_1.stroke_style = region["color"]
        scaled_x = region["x"] * self.scale_x
        scaled_y = region["y"] * self.scale_y
        scaled_width = region["width"] * self.scale_x
        scaled_height = region["height"] * self.scale_y
        self.canvas_1.stroke_rect(scaled_x, scaled_y, scaled_width, scaled_height)

    def canvas_mouse_down(self, x, y, button, **event_args):
        """Handle mouse clicks on the canvas."""
        # Adjust click coordinates back to natural image scale
        scaled_x = x / self.scale_x
        scaled_y = y / self.scale_y

        print(f"Mouse clicked at ({scaled_x}, {scaled_y})")  # Debugging

        # Check which region was clicked
        for region in self.regions:
            if (
                region["x"] < scaled_x < region["x"] + region["width"]
                and region["y"] < scaled_y < region["y"] + region["height"]
            ):
                alert(f"{region['name']} clicked!")
                return

        alert("Clicked outside any region.")
