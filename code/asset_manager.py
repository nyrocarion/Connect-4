import pygame
import os

class Asset_Manager(object):
    def __init__(self):
        pygame.font.init()
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        # Fonts
        title_font_path = os.path.join(root_dir, "assets", "fonts", "Daydream.ttf")
        title_font_big = pygame.font.Font(title_font_path,50)
        title_font = pygame.font.Font(title_font_path,50)
        medium_title_font = pygame.font.Font(title_font_path,25)
        medium_title_font_2 = pygame.font.Font(title_font_path,28)
        self.fonts = {
            "title_font_big" : title_font_big,
            "title_font" : title_font,
            "medium_title_font" : medium_title_font,
            "medium_title_font_bigger" : medium_title_font_2
        }
        # Sounds
        select_sound_path = os.path.join(root_dir, "assets", "sounds", "Select_Sound_Whistle.mp3")
        select_sound = pygame.mixer.Sound(select_sound_path)
        hover_sound_path = os.path.join(root_dir, "assets", "sounds", "Hover_Sound.wav")
        hover_sound = pygame.mixer.Sound(hover_sound_path)
        self.sounds = {
            "select" :  select_sound,
            "hover" : hover_sound
        }
        # Music
        intro_music_path = os.path.join(root_dir, "assets", "sounds", "Intro_Song.wav")
        self.music = {
            "title" : intro_music_path
        }

    def get_fonts(self):
        return self.fonts
    
    def get_sounds(self):
        return self.sounds
    
    def get_music(self):
        return self.music