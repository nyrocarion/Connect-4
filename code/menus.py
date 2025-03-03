import pygame

def get_middle():
    width, height = pygame.display.get_window_size()
    center = (width//2,height//2)
    return center

class Start_Screen(object):
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
        pygame.display.set_caption('Welcome to Connect 4 by nyronik')
        title_text = "Connect 4!"
        enter_text = "Press Enter"

        title = self.fonts["title_font"].render(title_text,True,"white")
        title_shadow = self.fonts["title_font"].render(title_text,True,"#7F7F7F")
        title_size = self.fonts["title_font"].size(title_text)
        title_pos = (get_middle()[0]-(title_size[0]/2),get_middle()[1]-(title_size[1]/2))

        enter = self.fonts["medium_title_font"].render(enter_text,True,"white")
        enter_big = self.fonts["medium_title_font_bigger"].render(enter_text,True,"white")

        counter = 0
        pygame.mixer.music.load(self.background_music)
        pygame.mixer.music.play(-1)
        while self.running:
            counter = (counter + 1)%20
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    self.running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
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
        pygame.mixer.music.stop()
        pygame.time.wait(20)
        pygame.mixer.Sound.play(self.sounds["select"])
        pygame.time.wait(350)

