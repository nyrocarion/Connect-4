import pygame
from code.menus import Start_Screen
from code.asset_manager import Asset_Manager

class Main(object):
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.screen = pygame.display.set_mode((1400, 1000))

        self.asset_manager = Asset_Manager()
        start_screen = Start_Screen(self.screen,self.asset_manager)
        self.running = True
        self.mainloop()

    def mainloop(self):
        pygame.display.set_caption('Connect 4')
        while self.running:
            self.clock.tick(self.fps)
            # Responsible for reading keyboard inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    self.running = False
                    pygame.quit()
            self.screen.fill((0,0,0))
            pygame.display.flip()

# Start the game if this file is run
if __name__ == "__main__":
    m = Main()
    m.mainloop()