# Script to access shooter-bubble.de

import webbrowser
import subprocess
import pyautogui
import time
import random

# URL of the game
game_url = 'https://www.shooter-bubble.de/'

# Open a new Firefox window and navigate to the game
webbrowser.get('chromium').open_new(game_url)

# Wait a moment to ensure the browser has started
time.sleep(2.5)

# Bring the Firefox window to the front
subprocess.run(["wmctrl", "-a", "Chromium"])

# shoot a random bubble

time.sleep(2.5)

# Turn off sound
pyautogui.moveTo(941, 481)
pyautogui.click()

# Coordinates of the upper left and lower right corners
upper_left_x = 294
upper_left_y = 389
lower_right_x = 837
lower_right_y = 850

# Randomly choose a point within the specified area
click_x = random.randint(upper_left_x, lower_right_x)
click_y = random.randint(upper_left_y, lower_right_y)

# Move the mouse to the chosen point and click
pyautogui.moveTo(click_x, click_y)
pyautogui.click()

# Optionally, add a delay
time.sleep(1)