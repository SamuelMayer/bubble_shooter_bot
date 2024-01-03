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

# Samsung Monitor
click_area_Samsung = {'upper_left': (300, 400), 'lower_right': (800, 850)}
Sound_off_Samsung = {940, 480}

# MacBook Trisha
click_area_Mac = {'upper_left': (300, 400), 'lower_right': (800, 850)}
Sound_off_Mac = {940, 480}

# Laptop Sam
click_area_Asus = {'upper_left': (300, 400), 'lower_right': (800, 850)}
Sound_off_Asus = {940, 480}

# Example usage
click_area = {'upper_left': (300, 400), 'lower_right': (800, 850)}
sound_off_coords = (940, 480)
game = GameController(url=website_url, click_area=click_area, sound_off_coords=sound_off_coords)
game.open_game()
game.turn_off_sound()
game.random_click_in_game()