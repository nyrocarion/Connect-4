# Libraries
import pygame
#from code.whatever import whatever

class Main(object):
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.screen = pygame.display.set_mode((1000, 1000))
        pygame.display.set_caption('Connect 4')
        self.running = True

    def mainloop(self):
        while self.running:
            self.clock.tick(self.fps)
            # Responsible for reading keyboard inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    self.running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.inputs["right"] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.inputs["right"] = False

            self.screen.fill((0,0,0))
            pygame.display.flip()

# Start the game if this file is run
if __name__ == "__main__":
    m = Main()
    m.mainloop()