import webbrowser
import subprocess
import pyautogui
import time
import random

class GameController:
    def __init__(self, url, browser='chromium'):
        self.url = url
        self.browser = browser
        self.click_area = click_area if click_area else {'upper_left': (294, 389), 'lower_right': (837, 850)}
        self.sound_off_coords = sound_off_coords if sound_off_coords else (941, 481)


    def open_game(self):
        """Opens the game in a specified browser window."""
        webbrowser.get(self.browser).open_new(self.url)
        time.sleep(1.5)
        subprocess.run(["wmctrl", "-a", self.browser.title()])
        time.sleep(1.5)

    def turn_off_sound(self):
        """Turns off the sound in the game."""
        pyautogui.moveTo(941, 481)
        pyautogui.click()

    def random_click_in_game(self):
        """Performs a random click within the specified game area."""
        upper_left_x, upper_left_y = self.click_area['upper_left']
        lower_right_x, lower_right_y = self.click_area['lower_right']
        click_x = random.randint(upper_left_x, lower_right_x)
        click_y = random.randint(upper_left_y, lower_right_y)
        pyautogui.moveTo(click_x, click_y)
        pyautogui.click()

# Example usage
game = GameController('https://www.shooter-bubble.de/')
game.open_game()
game.turn_off_sound()
game.random_click_in_game()
