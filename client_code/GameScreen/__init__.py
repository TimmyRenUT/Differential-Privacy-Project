from anvil import *
import anvil
from anvil import URLMedia
from ._anvil_designer import GameScreenTemplate
import anvil.server

class GameScreen(GameScreenTemplate):
    def __init__(self, **properties):
        # Initialize the form
        self.init_components(**properties)
        self.url = server.get_app_origin()
        # URL for the labeled map image
        self.map_url = f"{self.url}/_/theme/labeled_map.png"

        # Canvas size
        self.canvas_1.width = 800
        self.canvas_1.height = 600
        self.clues_data = {
    'Vault': {
        1: '''Aiden's Diary: The vault was trashed, and an enchanted Netherite sword is missing. The robber used a diamond tool to escape unseen.''',
        2: '''Aiden's Diary: The vault was tahsedr, and an ecannethd Netherite sword is missing. The rebobr used a danmoid tool to ecaspe unseen.''',
        3: '''Aiden's Driya: The vlaut was tdaeshr, and an enchanted Nhtietere sword is missing. The robber uesd a dnmioad tool to escape uennse.''',
        4: '''A'idnes Driya: The vault was thseard, and an enaetnhcd Nihrettee sorwd is msnsiig. The rbeobr used a dianmod tool to eacspe unnees.''',
        5: '''sAnid'e iDrya: eTh avltu swa ardehts, and an adenecthn trheieNte rwsdo si siimsgn. ehT borrbe eusd a didonma ltoo ot eaescp esneun.''',
        6: '''iseGAn'd ayrODi: heTe vtfual svwa stehNadr, nIad aNn adcehetnnh tNehwetrie odVsrw sQi imssEngi. ejhT rbbOore esldu Da onmpddai loUot tLo pceisae eeuCsnn.''',
        7: '''dniaGAs'e ryiywaD: eSnhT uthealv sRdwa radhWZset, nrNda aEin etaneSdhcne rtetuqeheiN dolVrsw scGi mgisJgnis. hAjeT oerVlrbb edMfsu wpa doaQlmind toHlol oaDt spcCDeea esnsmeun.''',
        8: '''nsiNpldA'e aiDZdTry: hJfVeT vteRjaul aQSCws searSZNhtd, dngtna anEfn ennewDIhdtca teriDRHehetN odCnYwrs iHcvs isgmJPJnis. hLceeT rebwJUrbo edtMnus xPva oddtpinami otnwgol oMUXt acsTNtpee senSnsenu.''',
        9: '''esnADamdA'i iayWSHgrD: eEdGVTh vtExTDalu shNrbaw resaYfCPdht, dyWlean anRzFn tcnnvJFkeedah rteiWpDUetNhe rdnkJpsow szIqoi nmishlXYigs. enzvmhT rrbCseHboe edixGous pugEa dadhvFomion oocszrlt tEavZo seajLYBcep nunmtMTese.''',
        10: '''bcDfsMk tvCbxD Aau RquDq AZy msUtpnAK VSP XS UXFQKOXll ZKsfcCjLe aXeNa GB URKTtDrh doc OPTLmY cdqK P guymsyX zdVz Hu wlciFt cSmaEGV''',
    },
    'Potion Shop': {
        1: '''Customer Note: Sophie spent all night brewing potions to save Ethan after his epic battle with a wither.''',
        2: '''Customer Note: Sphioe spent all ngiht brewing potions to save Ethan after his epic baltte with a wrhite.''',
        3: '''Customer Neto: Sophie snpet all nhgit brewing potions to svae Ethan after his epic battle with a whteir.''',
        4: '''Csteoumr Ntoe: Spoihe spnet all nhigt bnewrig pootnis to svae Etahn aeftr his epic btatle with a wteihr.''',
        5: '''remousCt etoN: eSipoh snpet all ntghi inbgrwe tnooips to seav htnEa eraft his peic labtet itwh a irwteh.''',
        6: '''rseuImCot toWNe: ipoKehS perstn lVal itlnhg wniNrebg tnsHpooi oKt savev taInEh teIarf sEhi ecCip bltXeta tifhw Na tihzwre.''',
        7: '''CreszUtoum otMaNe: eSibfhpo tpYfnes lVTal nhcntig webICnirg tooiDispn tSmo aepJsv ntRqhEa ftuDare icyhs epmAic aebJjtlt itjmhw FKa whrgNeti.''',
        8: '''toreQArumCs eoATVNt: hSofudpie npxWhtes aiQill igkFfhnt rbeZPHwign stoeMKnpio ocFlt vsIzwae anjiBhEt arLZntef ifZchs eckphpi abtXwRlte whnibti Ovra tiwZTMreh.''',
        9: '''smueMPvbtrCo tNPGUGeo: SpejegQhoi ntaLoppse lLBoDla tgoeRfinh bernwNnwign noiNQunpsot tNAlIo svzhfGae EawtxLnht afcfkPtre sKewAhi ecxNQHip ltbBkVEtea whFQPUit fjZea iweDltQhrt.''',
        10: '''ccyHWgzt KMXbt LqvlfM ZCtTI KkF uAloQ GeCiejk CKzxMwR mJ jHoy PXvWV CdnaP dJo xmJL FGaEKz RHmD n XQDNKfb''',
    },
    'Library': {
        1: '''Lucas's Diary: I spent all night comforting Gavin, he saw the robber rob the armor shop and charge toward his garden.''',
        2: '''Lucas's Diary: I spent all ngiht comforting Gavin, he saw the roebbr rob the aomrr shop and chgare toward his gaedrn.''',
        3: '''Lucas's Draiy: I spnet all night comforting Gvain, he saw the rbboer rob the armor sohp and cahgre toward his garden.''',
        4: '''Lsca'us Driay: I spent all ngiht ctomfinrog Gnvia, he saw the rebbor rob the amror sohp and chrgae toarwd his gedanr.''',
        5: '''cauLs's iaryD: I spetn lla gnthi icmonftrgo vanGi, he aws het ebrrob orb eth amrro psoh adn ehgrca dtoraw hsi edgarn.''',
        6: '''ucaSsL's yaivrD: KI nePtps lnla hgDtni cgmrooinoft anGivi, eJh adws tqhe eboGbrr okbr hlte rawmro spsoh aHnd ergRcah rtwPdoa sHih aeridgn.''',
        7: '''aLsWEsu'c iryRADa: VZI psDcnte aoOll thDyngi mofrgLQitocn anGhkiv, hEhe sWgwa eIqht bbeaMorr oDzbr tkleh rrYNaom osrgph aiund rgaURech daruNtwo hCHsi rgdydean.''',
        8: '''acsDQXuL's ryaDfQDi: zjbI teCfxpsn aoRlll nhEstitg tfnmcVGvgrioo iGvUwCan, evjnh sopNaw eafKth borxVZber bwPbro tLhneh arooumro hoswTsp axdKdn carNmvghe atoCOxwdr iyuIhs nreWOEdag.''',
        9: '''csuFlQzsa'L DirNDufay: BcRyI ntsRpdesp aORIhll htiaapgin ftronVqkviocmg GnimVNFav, eCkFLh wLxaaas hnbVLet brbhfNCoer ouWYprb hmLWZte maWsfErro hoIDkYps aQvrwdn ghcpOwqera twoYHLVrda hFYevsi rgeZydUnad.''',
        10: '''lLMUtLi pFTavT X bYmAd lZb CkgrS oNXRsbjCvY gnkSpJ Tl Vln TUL sCthCH gMw TIx vtyvR KZQX zjG fuKjPl SniMUW jOS GEiSmtC''',
    },
}
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
                "y": 20,
                "width": 250,
                "height": 250,
                "type": "text",
                "content": "The vault was trashed, and an enchanted Netherite sword is missing. The robber used a diamond tool to escape unseen."
            },
            "Garden": {
                "name": 'Garden',
                "x": 50,
                "y": 560,
                "width": 550,
                "height": 270,
                "type": "image",
                "content": "garden.png"
            },
            "Potion Shop": {
                "name": 'Potion Shop',
                "x": 1080,
                "y": 380,
                "width": 200,
                "height": 150,
                "type": "text",
                "content": "Sophie spent all night brewing potions to save Ethan after his epic battle with a wither."
            },
            "Library": {
                "name": 'Library',
                "x": 600,
                "y": 360,
                "width": 200,
                "height": 150,
                "type": "text",
                "content": "Lucas spent all night comforting Gavin, who witnessed the robber rob the armorsmith and charge toward his garden."
            },
            "Armor Shop": {
                "name": 'Armor Shop',
                "x": 850,
                "y": 460,
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
        #print("Timer tick triggered.")  # Debugging
        self.timer_1.set_event_handler("tick", None)  # Disable the timer
        self.timer_1.enabled = False
        self.load_map()

    def show_map(self):
        """
        Show the map and hide clue components.
        """
        #print("Showing map...")  # Debugging
        self.canvas_1.visible = True
        self.label_noise_level.visible = True
        self.button_back_to_map.visible = False
        self.canvas_1.clear_rect(0, 0, self.canvas_1.width, self.canvas_1.height)

        # Draw the map
        self.load_map()


    def load_clue_tick(self, **event_args):
        """
        Timer tick to load the clue after a short delay.
        """
        #print("Loading clue...")  # Debugging
        self.timer_1.enabled = False  # Disable the timer
        self.timer_1.set_event_handler("tick", None)  # Unset the timer event

        # Clear the canvas
        self.canvas_1.clear_rect(0, 0, self.canvas_1.width, self.canvas_1.height)

        # Render the clue based on type
        if self.current_region["type"] == "text":
            #print("Rendering text clue...")  # Debugging
            self.display_clue_book(self.current_region["content"])
        elif self.current_region["type"] == "image":
            #print("Rendering image clue...")  # Debugging
            self.display_clue_image(self.current_region["content"])
    
    def display_clue_book(self, region_name):
        """
        Display the text clue for the specified region and current noise level.
        """
        # Get the current noise level
        noise_level = max(1, min(self.game_state["noise_level"], 10))  # Ensure noise level is within bounds
    
        # Fetch the degraded text from self.clues_data
        degraded_text = self.clues_data.get(region_name, {}).get(noise_level, "No clue available for this region.")
    
        # Clear the canvas
        self.canvas_1.clear_rect(0, 0, self.canvas_1.width, self.canvas_1.height)
    
        # Show the "Back to Map" button
        self.button_back_to_map.visible = True
    
        book_image_url = f"{self.url}/_/theme/minecraft_book.png"
        canvas_width = self.canvas_1.width
        canvas_height = self.canvas_1.height
    
        # Define the desired book dimensions (e.g., 50% width, 70% height of the canvas)
        book_width = canvas_width * 0.35
        book_height = canvas_height * 0.7
    
        # Calculate position to center the book
        book_x = (canvas_width - book_width) / 2
        book_y = (canvas_height - book_height) /2 -100
    
        try:
            #print(f"Loading book image from {book_image_url}...")  # Debugging
            image = anvil.URLMedia(book_image_url)
            self.canvas_1.clear_rect(0, 0, canvas_width, canvas_height)  # Clear previous content
            self.canvas_1.draw_image(image, book_x, book_y, book_width, book_height)
            #print("Book image rendered.")  # Debugging
        except Exception as e:
            print(f"Error rendering book image: {e}")
    
        try:
            # Adjust text position and size relative to the scaled book
            self.canvas_1.fill_style = "#000000"  # Black text
            self.canvas_1.font = "14px Tiny5"  # Smaller font for better fit
            text_x = book_x + book_width * 0.1 + 20  # Add padding inside the book
            text_y = book_y + book_height * 0.2 -10
            line_height = 20
            max_line_length = 30
    
            # Wrap and render text inside the book
            words = degraded_text.split()
            line = ""
            for word in words:
                test_line = f"{line} {word}".strip()
                if len(test_line) <= max_line_length:
                    line = test_line
                else:
                    self.canvas_1.fill_text(line, text_x, text_y)
                    text_y += line_height
                    line = word
            if line:
                self.canvas_1.fill_text(line, text_x, text_y)
            #print("Clue text rendered successfully.")
        except Exception as e:
            print(f"Error rendering clue text: {e}")

    def display_clue_image(self, image_name):
        """
        Display an image-based clue, selecting the appropriate blur level based on the noise level.
        """
        self.button_back_to_map.visible = True
        # Determine the current noise level (clamp between 1 and 10 to match the assets)
        noise_level = max(1, min(self.game_state["noise_level"], 10))
        
        # Construct the image name based on the noise level
        image_file = image_name.replace(".png", f"_blurred_level_{noise_level}.png")
        image_url = f"{anvil.server.get_app_origin()}/_/theme/{image_file}"
        
        canvas_width = self.canvas_1.width
        canvas_height = self.canvas_1.height
    
        try:
            #print(f"Loading clue image from {image_url}...")  # Debugging
            image = anvil.URLMedia(image_url)
            self.canvas_1.clear_rect(0, 0, canvas_width, canvas_height)  # Clear previous content
            self.canvas_1.draw_image(image, 0, 0, canvas_width, canvas_height)
            #print("Clue image rendered successfully.")  # Debugging
        except Exception as e:
            print(f"Error rendering clue image: {e}")

        if image_name == 'armory.png':  
          try:
              # Draw the "It appears something was stolen..." message on the canvas
              self.canvas_1.fill_style = "#ffffff"
              self.canvas_1.font = "45px Tiny5"
              self.canvas_1.fill_text("It appears something was stolen...", 30, 75)  # Top left position
          except Exception as e:
              print(f"Error rendering text on canvas: {e}")
      

    def update_noise_level_display(self):
        """
        Update the noise level label on the screen.
        """
        self.label_noise_level.text = f"Noise Level: {self.game_state['noise_level']}"
    
    def canvas_mouse_down(self, x, y, button, **event_args):
        scaled_x = x / self.scale_x
        scaled_y = y / self.scale_y
    
        for region_name, region_data in self.regions.items():
            if (
                region_data["x"] < scaled_x < region_data["x"] + region_data["width"]
                and region_data["y"] < scaled_y < region_data["y"] + region_data["height"]
            ):
                #print(f"{region_name} clicked!")  # Debugging
                self.game_state["noise_level"] += 1
                self.update_noise_level_display()
                self.disable_canvas_mouse_down()
                if region_data["type"] == "text":
                    self.display_clue_book(region_name)
                elif region_data["type"] == "image":
                    self.display_clue_image(region_data["content"])  # Pass the image name
                return


    def button_back_to_map_click(self, **event_args):
        """
        Handle 'Back to Map' button click.
        """
        #print("Returning to map...")  # Debugging
        self.canvas_1.visible = True
        self.button_back_to_map.visible = False
        self.enable_canvas_mouse_down()
        # Reset the timer to delay map loading
        self.timer_1.set_event_handler("tick", self.reload_map_tick)
        self.timer_1.interval = 0.1
        self.timer_1.enabled = True
    
    def reload_map_tick(self, **event_args):
        """
        Timer tick to reload the map after returning from clue view.
        """
        #print("Reloading map...")  # Debugging
        self.timer_1.enabled = False
        self.timer_1.set_event_handler("tick", None)
        self.show_map()
    
    def load_map(self):
        """Load and scale the map image onto the canvas."""
        #print("Attempting to load the map image...")  # Debugging
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
            draw_y = (canvas_height - draw_height) / 2 -75
    
            self.canvas_1.clear_rect(0, 0, canvas_width, canvas_height)
            self.canvas_1.draw_image(image_media, draw_x, draw_y, draw_width, draw_height)
            #print("Map loaded and drawn successfully.")
        except Exception as e:
            print(f"Error loading map: {e}")

    def disable_canvas_mouse_down(self):
        """
        Disable the canvas mouse_down event handler.
        """
        self.canvas_1.set_event_handler("mouse_down", None)

    def enable_canvas_mouse_down(self):
        """
        Enable the canvas mouse_down event handler.
        """
        self.canvas_1.set_event_handler("mouse_down", self.canvas_mouse_down)

    def button_1_click(self, **event_args):
      if self.drop_down_1.selected_value == 'Mason':
        open_form('Form1')
      else:
        alert('Hmmmm that does not seem to be the correct person, try finding more information and select someone else')
