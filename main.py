import webbrowser
import subprocess
import pyautogui
import time
import random
from GameController import GameController

# Bubble Shooter 
website_url = "https://www.shooter-bubble.de/"

############################################################################
# Pixel Vectors to adjust for different Monitors
############################################################################

# Samsung Monitor################################
click_area_Samsung = {'upper_left': (300, 400), 'lower_right': (800, 850)}
Sound_off_Samsung = {940, 480}

# MacBook Trisha
click_area_Mac = {'upper_left': (300, 400), 'lower_right': (800, 850)}
Sound_off_Mac = {940, 480}

# Laptop Sam
click_area_Asus = {'upper_left': (415, 415), 'lower_right': (950, 880)}
Sound_off_Asus = {1060, 510}

# Example usage

# Example usage
game = GameController('https://www.shooter-bubble.de/', template_path='images/sound_off_button.png')
game.open_game()
game.click_image()
#Open Game
#Turn off Sound
#game.click_button(image = 'images/sound_off_button.png', scaling=0.9)
# Click random point in Game
game.random_click_in_game()