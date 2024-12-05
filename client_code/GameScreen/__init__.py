from anvil import *
import anvil
from anvil import URLMedia
from ._anvil_designer import GameScreenTemplate


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
        self.clues_data = {
    'Vault': {
        1: '''Aiden's Diary: The vault was trashed, and an enchanted Netherite sword is missing. The robber used a diamond tool to escape unseen.''',
        2: '''Aiden's Diary: The vault was tdraehs, and an eceathnnd Netherite sword is missing. The robebr used a danmiod tool to espace unseen.''',
        3: '''Aiden's Dyria: The vault was tdrehas, and an enchanted Ntheritee sword is missing. The robber used a donmaid tool to escape uennse.''',
        4: '''Ad'ines Diyar: The valut was tdrehas, and an eenhnactd Ntheietre sword is msiigns. The rbebor used a daniomd tool to epacse uesnne.''',
        5: '''edAni's iraDy: ehT tauvl aws hdrtaes, adn an anntehecd etertiNhe rowds si imngsis. ehT erobbr edus a maidndo tool ot scaepe nnusee.''',
        6: '''nsdpAe'i rDiway: hOeT ltvauv aUsw sdaeMthr, dpna nLa enhaxcnedt eeitWtehNr solwdr ims migsqsni. eehT rebgbor edSsu Ca daoPmndi toNlo oHt espueac esnTuen.''',
        7: '''sinycAe'd Driulay: ekChT vtyDual aNisw rtedgVhsa, dJtan ahDn etcePNhdann tieeSMtNher sriMowd iCJs giintIsms. TSqhe beoVcbrr suOKed FDa maiVsdodn tlkxoo tavo aspbicee ensXguen.''',
        8: '''dAnalPsi'e riyOoYDa: Tkkuhe avzYltlu aSFVsw srthSWGaed, aHzsdn nIhka dnecYwxtnahe ereNGrmttihe roLtUwsd iBsts ngmsHeViis. eiJaTh orbEjLbre duwXles XNwa mdiPwtndoa toMQvlo tKhSo pacXYuese nesLJineu.''',
        9: '''indEwtHse'A airBrrAyD: ewrTITh atZjOFlvu wqAPCsa hastmoPfder, agJGSdn nwrYpa actnKevynedhe theeAcRYeNrit woMQVYsdr sSwfti sgiscAVUnim. elIoPhT brojfDYerb edwASEus LCtxa iddBhnhaonm loIxEuto tMOeco sapRlZrece eesocDEunn.''',
        10: '''cMcyVbT NqGiJY rbb tIZVQ GMG gPtiYQfB bQr xJ LcFtqSJMn tAAySkgAD RpZjx qi mtlkMpVr bjS DWwrvx MXKP r yaUVLrs Eryk QV KUWzbJ wsnDSqE''',
    },
    'Potion Shop': {
        1: '''Customer Note: Sophie spent all night brewing potions to save Ethan after his epic battle with a wither.''',
        2: '''Customer Note: Sophie spent all nhigt brewing potions to save Ethan after his epic btalte with a witerh.''',
        3: '''Customer Nteo: Sophie spent all night brewing pntioos to save Ethan atfer his epic battle with a wrtihe.''',
        4: '''Coetmusr Ntoe: Shopie spnet all nghit binewrg poitnos to save Ethan after his eipc bltate wtih a wherti.''',
        5: '''rosCemtu Neto: iphoSe tensp all nhigt bigrewn ntspoio to evsa Enath rfeat shi eipc ttblea with a erwith.''',
        6: '''CrmtIoeus toSeN: hSeMpoi etWnsp lkal ihxtng breBgnwi tpiboons tco evksa nEptha taPref hlsi icFep tteyabl iwRth ga erthwhi.''',
        7: '''CtumMcoers otKoeN: ehiYMopS psLFten lySla ngDViht rbnxqwegi oipBKntso tFqo sepNav aEamnth afazter hxgis pemdic abtNAelt hiyEtw cCa htitGerw.''',
        8: '''utosUlGmCre otfJneN: SeilAyhop ptOXusne amUYll hnmowigt nriCOybegw nopLCyitos oCWht saaqOve nhFlHtEa efVVqart hWjbsi ieYEOpc tebreftla ihmRswt cmTa tirmTEehw.''',
        9: '''meCutvOCsrot NeMBhLto: oipEKnmSeh eskBhtnpt lRXbLla ghxPDEitn biwWlbsengr tisPgFznopo tSnono veuNNZas EtKHIjahn etziQKfra sBMTfih ipVTWeec eatmhaublt whkEyCti JlHva iwhgHQlter.''',
        10: '''vyrbkWfc Mzzrf oeVafr YVtxi reP MuwlU oksQUHk QWxKAxM mL qxsQ eiNkL yDmaY WfH xWsK AlEvJV Sbva M dKInRYO''',
    },
    'Library': {
        1: '''Lucas's Diary: I spent all night comforting Gavin, he saw the robber rob the armorsmith and charge toward his garden.''',
        2: '''Lucas's Diary: I spent all nghit comforting Gavin, he saw the rebbor rob the atsrrimmoh and charge traowd his garden.''',
        3: '''Lucas's Dyria: I sepnt all nhgit comforting Ganiv, he saw the rbebor rob the armorsmith and charge tawrod his grnead.''',
        4: '''L'uacss Diayr: I sepnt all nghit cnfotimrog Gavin, he saw the rboebr rob the aromstmrih and cahrge troawd his gdrnea.''',
        5: '''acuss'L yDari: I tpens all thnig fcogmotrni anivG, he saw het rerbob rbo eht aihmtorsmr and rhgcea woradt his gndrea.''',
        6: '''ussQLa'c arDNyi: CI sewntp lgal htyngi fiomcZnotrg inaTGv, eMh aysw hxte ebrJbor bNro tkhe armmtxihsor aRnd eaghrch rwdFtoa iosh gnrtade.''',
        7: '''sasCzLu'c DayBKri: ClI esiUtnp lXDal hikggtn ocmtrqfniogf vGijCna, hfCe wMGsa ekWht erbjlbor ooXbr hzvet somamAdrthir adHnd ehcxlrag tdwWTora sYKhi dannwerg.''',
        8: '''sLcnoVas'u aiDRTDry: moXI epfLAnst lrlUal tgAQQnhi octomnoqrfgni vaGGXTin, eBtMh sCqiaw eNXRth rbrbNjboe oDZGrb tlLChe tahmsjKfmiror nLmnad raeBvHgch otrvaddaw sOQRih eagXnednr.''',
        9: '''csaGeClsL'u iayCPwkDr: ntSPI nsZvGzetp lVSGJal ntRWqShgi oftoifPxHgnmcr GivrTaDan, hrjrme akRyjws eDofMth rrbsyTjeob rmHejbo tbUvzeh oarrmAoRMimtsh nJtwyad hrgozMCeac dawZoUutro hPoXcis gdrtbpeean.''',
        10: '''gGUwFgl ZRbYbk s mmZHQ enm vINcE uRqTmowdWH LIpzGd EL PyY LDc roeyEG Xve rNe IDYqQRwqZu zuY dCnWXc zVaeWZ oqM LCaWuql''',
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
    
        # Draw the book background image
        book_image_url = f"{anvil.server.get_app_origin()}/_/theme/minecraft_book.png"
        book_image = anvil.URLMedia(book_image_url)
        canvas_width = self.canvas_1.width
        canvas_height = self.canvas_1.height
        book_width = canvas_width * 0.35
        book_height = canvas_height * 0.7
        book_x = (canvas_width - book_width) / 2
        book_y = (canvas_height - book_height) / 2 - 100
    
        self.canvas_1.draw_image(book_image, book_x, book_y, book_width, book_height)
    
        # Render the degraded text on the canvas, ensuring line breaks are respected
        self.canvas_1.fill_style = "#000000"
        self.canvas_1.font = "14px sans-serif"
        text_x = book_x + book_width * 0.1
        text_y = book_y + book_height * 0.2
        line_height = 20
        max_line_width = book_width * 0.8  # Limit text width to fit inside the book
    
        for line in degraded_text.splitlines():
            words = line.split()
            current_line = ""
    
            for word in words:
                # Check if adding the next word would exceed the line width
                if self.canvas_1.measure_text(current_line + " " + word).width > max_line_width:
                    # Draw the current line and reset
                    self.canvas_1.fill_text(current_line.strip(), text_x, text_y)
                    text_y += line_height
                    current_line = word
                else:
                    current_line += " " + word
    
            # Draw any remaining text in the current line
            if current_line:
                self.canvas_1.fill_text(current_line.strip(), text_x, text_y)
                text_y += line_height
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
