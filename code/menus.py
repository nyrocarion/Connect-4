import pygame

GREY = "#707078"
BLACK = "#000000"
WHITE = "#FFFFFF"
ORANGE = "#EC4E20"
YELLOW = "#FF9505"

def get_middle():
    width, height = pygame.display.get_window_size()
    center = (width//2,height//2)
    return center

def get_screen_dim():
    width, height = pygame.display.get_window_size()
    return (width,height)

class Start_Screen(object):
    def __init__(self,main):
        self.main = main
        self.running = True
        self.screen = self.main.get_screen()
        self.fonts = self.main.get_asset_manager().get_fonts()
        self.background_music = self.main.get_asset_manager().get_music()["title"]
        self.sounds = self.main.get_asset_manager().get_sounds()
        self.clock = pygame.time.Clock()
        self.fps = 20
        self.loop()

    def loop(self):
        pygame.display.set_caption('Welcome to Connect 4 by nyronik')
        title_text = "Connect 4!"
        enter_text = "Press Enter"

        title = self.fonts["title_font"].render(title_text,True,WHITE)
        title_shadow = self.fonts["title_font"].render(title_text,True,GREY)
        title_size = self.fonts["title_font"].size(title_text)
        title_pos = (get_middle()[0]-(title_size[0]/2),get_middle()[1]-(title_size[1]/2))

        enter = self.fonts["medium_title_font"].render(enter_text,True,WHITE)
        enter_big = self.fonts["medium_title_font_bigger"].render(enter_text,True,WHITE)

        counter = 0
        pygame.mixer.music.load(self.background_music)
        pygame.mixer.music.play(-1)
        start_next_menu = False
        while self.running:
            counter = (counter + 1)%20
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    self.running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        start_next_menu = True
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        
                    
            self.screen.fill((0,0,0))
            # Blit Text
            self.screen.blit(title_shadow,(title_pos[0]+5,title_pos[1]+5))
            self.screen.blit(title,title_pos)
            if counter <= 10:
                enter_size = self.fonts["medium_title_font_bigger"].size(enter_text)
                enter_pos = (get_middle()[0]-(enter_size[0]/2),get_middle()[1]-(enter_size[1]/2)+title_size[1]+10)
                self.screen.blit(enter_big,enter_pos)
            else:
                enter_size = self.fonts["medium_title_font"].size(enter_text)
                enter_pos = (get_middle()[0]-(enter_size[0]/2),get_middle()[1]-(enter_size[1]/2)+title_size[1]+10)
                self.screen.blit(enter,enter_pos)
            
            pygame.display.flip()
            if start_next_menu:
                start_next_menu = False
                Main_Menu(self.main)
        pygame.mixer.music.stop()
        pygame.time.wait(20)
        pygame.mixer.Sound.play(self.sounds["select"])
        pygame.time.wait(350)
    
class Main_Menu(object):
    def __init__(self,main):
        self.main = main
        self.running = True
        self.screen = self.main.get_screen()
        self.fonts = self.main.get_asset_manager().get_fonts()
        self.background_music = self.main.get_asset_manager().get_music()["title"]
        self.sounds = self.main.get_asset_manager().get_sounds()
        self.asset_manager = self.main.get_asset_manager()
        self.clock = pygame.time.Clock()
        self.fps = 20
        self.menu_options = ["Manage players","Difficulty","Leaderboard","Settings","Credits"]
        self.menu_calls = {
            "Manage players" : Players_Menu,
            "Difficulty" : Difficulty_Menu,
            "Leaderboard" : Leaderboard_Menu,
            "Settings" : Settings_Menu,
            "Credits" : Credits_Menu
        }
        self.loop()


    def loop(self):
        pygame.display.set_caption('Connect 4 Startmenu')
        
        title_text = "Connect 4!"
        title = self.fonts["title_font_big"].render(title_text,True,WHITE)
        title_shadow = self.fonts["title_font_big"].render(title_text,True,GREY)
        title_size = self.fonts["title_font_big"].size(title_text)
        title_pos = (get_middle()[0]-(title_size[0]/2),50)

        press_enter_text = "Press Enter"
        press_enter = self.fonts["medium_title_font"].render(press_enter_text,True,WHITE)
        press_enter_big = self.fonts["medium_title_font_bigger"].render(press_enter_text,True,WHITE)

        bottom_msg_text = "To start the game"
        bottom_msg = self.fonts["medium_title_font"].render(bottom_msg_text,True,WHITE)
        bottom_msg_size = self.fonts["medium_title_font"].size(bottom_msg_text)
        bottom_msg_pos = (get_middle()[0]-(bottom_msg_size[0]/2),get_screen_dim()[1]-50-bottom_msg_size[1])

        leave_text = "Press ESC to leave"
        leave = self.fonts["small_title_font"].render(leave_text,True,WHITE)
        leave_size = self.fonts["small_title_font"].size(leave_text)
        leave_pos = (50,50)

        menu_rect = pygame.rect.Rect( (0,0),(400,70))

        pygame.mixer.music.load(self.background_music)
        pygame.mixer.music.play(-1)
        counter = 0
        mouse_pos = pygame.mouse.get_pos()
        self.already_over_it = None
        game_start = False
        while self.running:
            clicked = False
            prev_mouse_pos = mouse_pos
            mouse_pos = pygame.mouse.get_pos()
            counter = (counter + 1)%20
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    self.running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if event.key == pygame.K_RETURN:
                        self.running = False
                        game_start = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicked = True
            self.screen.fill((0,0,0))
            # Blit Text
            self.screen.blit(title_shadow,(title_pos[0]+5,title_pos[1]+5))
            self.screen.blit(title,title_pos)
            self.screen.blit(bottom_msg,bottom_msg_pos)
            self.screen.blit(leave,leave_pos)
            if counter <= 10:
                press_enter_size = self.fonts["medium_title_font_bigger"].size(press_enter_text)
                press_enter_pos = (get_middle()[0]-(press_enter_size[0]/2),get_screen_dim()[1]-50-bottom_msg_size[1]-press_enter_size[1]-10)
                self.screen.blit(press_enter_big,press_enter_pos)
            else:
                press_enter_size = self.fonts["medium_title_font"].size(press_enter_text)
                press_enter_pos = (get_middle()[0]-(press_enter_size[0]/2),get_screen_dim()[1]-50-bottom_msg_size[1]-press_enter_size[1]-10)
                self.screen.blit(press_enter,press_enter_pos)

            # One menu point is 75 with shadow  
            # Seperated with 25 makes them 100 heigh
            # Center the 500 heigh block vertically
            for menu_point in self.menu_options:
                display_text = menu_point
                rect = menu_rect.copy()
                # Pos is topleft point of rect
                x = get_middle()[0]-200
                y = get_middle()[1]-250+(self.menu_options.index(menu_point)*100)
                bg_x = x+10
                bg_y = y+10
                moved_rect = rect.move(x,y)
                moved_bg_rect = rect.move(bg_x,bg_y)
                if moved_rect.collidepoint(mouse_pos):
                    if not self.already_over_it and not moved_rect.collidepoint(prev_mouse_pos):
                        self.already_over_it = True
                        pygame.mixer.Sound.play(self.sounds["hover"])
                        pygame.time.wait(10)
                    display_text = "> " + menu_point + " <"
                    if clicked:
                        pygame.mixer.Sound.play(self.sounds["select"])
                        pygame.time.wait(15)
                        print("You clicked ",menu_point)
                        if not self.menu_calls[menu_point]== None:
                            self.menu_calls[menu_point](self.screen,self.asset_manager)
                else:
                    if self.already_over_it:
                        self.already_over_it = False
                pygame.draw.rect(self.screen,ORANGE,moved_bg_rect)
                pygame.draw.rect(self.screen,YELLOW,moved_rect)
                menu_item_text = display_text
                menu_item = self.fonts["medium_title_font"].render(menu_item_text,True,WHITE)
                menu_item_size = self.fonts["medium_title_font"].size(menu_item_text)
                menu_item_pos = (get_middle()[0]-(menu_item_size[0]/2),y+35-menu_item_size[1]/2)
                self.screen.blit(menu_item,menu_item_pos)
            
            pygame.display.flip()
        pygame.mixer.music.stop()
        pygame.time.wait(20)
        pygame.mixer.Sound.play(self.sounds["select"])
        pygame.time.wait(350)
        if game_start:
            print("Game should now start")
        else:
            print("Escape was pressed")

class Settings_Menu(object):
    def __init__(self,screen,asset_manager):
        self.running = True
        self.screen = screen
        self.fonts = asset_manager.get_fonts()
        self.background_music = asset_manager.get_music()["title"]
        self.sounds = asset_manager.get_sounds()
        self.clock = pygame.time.Clock()
        self.fps = 20
        self.loop()

    def loop(self):
        pygame.display.set_caption('Connect 4 Settings')
        title_text = "Settings"
        title = self.fonts["title_font_big"].render(title_text,True,WHITE)
        title_shadow = self.fonts["title_font_big"].render(title_text,True,GREY)
        title_size = self.fonts["title_font_big"].size(title_text)
        title_pos = (get_middle()[0]-(title_size[0]/2),50)

        leave_text = "Press ESC to leave"
        leave = self.fonts["small_title_font"].render(leave_text,True,WHITE)
        leave_size = self.fonts["small_title_font"].size(leave_text)
        leave_pos = (get_middle()[0]-(leave_size[0]/2),get_screen_dim()[1]-50-leave_size[1])

        while self.running:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    self.running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            self.screen.fill((0,0,0))
            # Blit Text
            self.screen.blit(title_shadow,(title_pos[0]+5,title_pos[1]+5))
            self.screen.blit(title,title_pos)
            self.screen.blit(leave,leave_pos)
            
            pygame.display.flip()

class Credits_Menu(object):
    def __init__(self,screen,asset_manager):
        self.running = True
        self.screen = screen
        self.fonts = asset_manager.get_fonts()
        self.background_music = asset_manager.get_music()["title"]
        self.sounds = asset_manager.get_sounds()
        self.clock = pygame.time.Clock()
        self.fps = 20
        self.loop()

    def loop(self):
        pygame.display.set_caption('Connect 4 Credits')
        title_text = "Credits"
        title = self.fonts["title_font_big"].render(title_text,True,WHITE)
        title_shadow = self.fonts["title_font_big"].render(title_text,True,GREY)
        title_size = self.fonts["title_font_big"].size(title_text)
        title_pos = (get_middle()[0]-(title_size[0]/2),50)

        leave_text = "Press ESC to leave"
        leave = self.fonts["small_title_font"].render(leave_text,True,WHITE)
        leave_size = self.fonts["small_title_font"].size(leave_text)
        leave_pos = (get_middle()[0]-(leave_size[0]/2),get_screen_dim()[1]-50-leave_size[1])

        while self.running:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    self.running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            self.screen.fill((0,0,0))
            # Blit Text
            self.screen.blit(title_shadow,(title_pos[0]+5,title_pos[1]+5))
            self.screen.blit(title,title_pos)
            self.screen.blit(leave,leave_pos)
            
            pygame.display.flip()

class Leaderboard_Menu(object):
    def __init__(self,screen,asset_manager):
        self.running = True
        self.screen = screen
        self.fonts = asset_manager.get_fonts()
        self.background_music = asset_manager.get_music()["title"]
        self.sounds = asset_manager.get_sounds()
        self.clock = pygame.time.Clock()
        self.fps = 20
        self.loop()

    def loop(self):
        pygame.display.set_caption('Connect 4 Leaderboard')
        title_text = "Leaderboard"
        title = self.fonts["title_font_big"].render(title_text,True,WHITE)
        title_shadow = self.fonts["title_font_big"].render(title_text,True,GREY)
        title_size = self.fonts["title_font_big"].size(title_text)
        title_pos = (get_middle()[0]-(title_size[0]/2),50)

        leave_text = "Press ESC to leave"
        leave = self.fonts["small_title_font"].render(leave_text,True,WHITE)
        leave_size = self.fonts["small_title_font"].size(leave_text)
        leave_pos = (get_middle()[0]-(leave_size[0]/2),get_screen_dim()[1]-50-leave_size[1])

        while self.running:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    self.running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            self.screen.fill((0,0,0))
            # Blit Text
            self.screen.blit(title_shadow,(title_pos[0]+5,title_pos[1]+5))
            self.screen.blit(title,title_pos)
            self.screen.blit(leave,leave_pos)
            
            pygame.display.flip()

class Difficulty_Menu(object):
    def __init__(self,screen,asset_manager):
        self.running = True
        self.screen = screen
        self.fonts = asset_manager.get_fonts()
        self.background_music = asset_manager.get_music()["title"]
        self.sounds = asset_manager.get_sounds()
        self.clock = pygame.time.Clock()
        self.fps = 20
        self.loop()

    def loop(self):
        pygame.display.set_caption('Connect 4 Difficulty Settings')
        title_text = "Modify Difficulty"
        title = self.fonts["title_font_big"].render(title_text,True,WHITE)
        title_shadow = self.fonts["title_font_big"].render(title_text,True,GREY)
        title_size = self.fonts["title_font_big"].size(title_text)
        title_pos = (get_middle()[0]-(title_size[0]/2),50)

        leave_text = "Press ESC to leave"
        leave = self.fonts["small_title_font"].render(leave_text,True,WHITE)
        leave_size = self.fonts["small_title_font"].size(leave_text)
        leave_pos = (get_middle()[0]-(leave_size[0]/2),get_screen_dim()[1]-50-leave_size[1])

        while self.running:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    self.running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            self.screen.fill((0,0,0))
            # Blit Text
            self.screen.blit(title_shadow,(title_pos[0]+5,title_pos[1]+5))
            self.screen.blit(title,title_pos)
            self.screen.blit(leave,leave_pos)
            
            pygame.display.flip()

class Players_Menu(object):
    def __init__(self,screen,asset_manager):
        self.running = True
        self.screen = screen
        self.fonts = asset_manager.get_fonts()
        self.background_music = asset_manager.get_music()["title"]
        self.sounds = asset_manager.get_sounds()
        self.clock = pygame.time.Clock()
        self.fps = 20
        self.loop()

    def loop(self):
        pygame.display.set_caption('Connect 4 Player Management')
        title_text = "Manage Players"
        title = self.fonts["title_font_big"].render(title_text,True,WHITE)
        title_shadow = self.fonts["title_font_big"].render(title_text,True,GREY)
        title_size = self.fonts["title_font_big"].size(title_text)
        title_pos = (get_middle()[0]-(title_size[0]/2),50)

        leave_text = "Press ESC to leave"
        leave = self.fonts["small_title_font"].render(leave_text,True,WHITE)
        leave_size = self.fonts["small_title_font"].size(leave_text)
        leave_pos = (get_middle()[0]-(leave_size[0]/2),get_screen_dim()[1]-50-leave_size[1])

        while self.running:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    self.running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            self.screen.fill((0,0,0))
            # Blit Text
            self.screen.blit(title_shadow,(title_pos[0]+5,title_pos[1]+5))
            self.screen.blit(title,title_pos)
            self.screen.blit(leave,leave_pos)
            
            pygame.display.flip()