import pygame
from code.menus import Start_Screen
from code.menus import Main_Menu
from code.asset_manager import Asset_Manager

class Main(object):
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.screen = pygame.display.set_mode((1920, 900))

        self.asset_manager = Asset_Manager()
        self.mainloop()

    def get_asset_manager(self):
        return self.asset_manager
    
    def get_screen(self):
        return self.screen

    def mainloop(self):
        self.running = True
        pygame.display.set_caption('Connect 4')
        Start_Screen(self)
        print("Quit Game")
        '''
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
            pygame.display.flip()
        '''
# Start the game if this file is run
if __name__ == "__main__":
    m = Main()