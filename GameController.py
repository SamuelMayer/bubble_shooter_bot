import cv2
import numpy as np
import pyautogui
import webbrowser
import subprocess
import time
import random

class GameController:
    def __init__(self, url, click_area={'upper_left': (300, 400), 'lower_right': (800, 850)}, browser='chromium'):
        self.url = url
        self.browser = browser
        self.click_area = click_area

    def open_game(self):
        """Opens the game in a specified browser window."""
        webbrowser.get(self.browser).open_new(self.url)
        time.sleep(.5)
        subprocess.run(["wmctrl", "-a", self.browser])  # Adjusted to just use the browser name
        time.sleep(.5)

    def capture_screen(self):
        screen = pyautogui.screenshot()
        screen_np = np.array(screen)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
        return screen_gray

    def find_image_on_screen(self, template_path):
        """Finds the specified image on the screen."""
        template = cv2.imread(template_path, 0)
        if template is None:
            print("Template image could not be loaded.")
            return None
        screen_gray = self.capture_screen()
        res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val < 0.8:  # Adjust the threshold as needed
            print("Image not found.")
            return None
        match_center_x = max_loc[0] + template.shape[1] // 2
        match_center_y = max_loc[1] + template.shape[0] // 2
        return (match_center_x, match_center_y)
    
    def click_image(self, template_path):
        """Clicks on the specified image if found on the screen."""
        location = self.find_image_on_screen(template_path)
        if location:
            pyautogui.moveTo(location[0], location[1], duration=0.5)  # Added duration to the move action
            pyautogui.click()  # Perform the click

    def random_click_in_game(self):
        """Performs a random click within the specified game area."""
        upper_left_x, upper_left_y = self.click_area['upper_left']
        lower_right_x, lower_right_y = self.click_area['lower_right']
        click_x = random.randint(upper_left_x, lower_right_x)
        click_y = random.randint(upper_left_y, lower_right_y)
        pyautogui.moveTo(click_x, click_y, duration=0.5)  # Added duration to the move action
        pyautogui.click()

# Example usage:
# game_controller = GameController(url="http://example.com", browser="chromium")
# game_controller.click_image('path/to/your/image.png')
