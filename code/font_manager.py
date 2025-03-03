import pygame
import os

class Font_Manager(object):
    def __init__(self):
        pygame.font.init()
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        title_font_path = os.path.join(root_dir, "assets", "fonts", "Daydream.ttf")
        title_font = pygame.font.Font(title_font_path,50)
        medium_title_font = pygame.font.Font(title_font_path,25)
        medium_title_font_2 = pygame.font.Font(title_font_path,28)
        self.fonts = {
            "title_font" : title_font,
            "medium_title_font" : medium_title_font,
            "medium_title_font_bigger" : medium_title_font_2
        }

    def get_fonts(self):
        return self.fonts