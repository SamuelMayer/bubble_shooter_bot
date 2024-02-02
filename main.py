import webbrowser
import subprocess
import pyautogui
import time
import random
import cv2
from GameController import GameController
# from OCR import OCRClass
from digit_classifier import MultiDigitRecognizer

# Define the website URL for Bubble Shooter
website_url = "https://www.shooter-bubble.de/"

# Pixel Vectors to adjust for different Monitors
click_areas = {
    'Samsung': {'upper_left': (300, 400), 'lower_right': (800, 850)},
    'MacBook_Trisha': {'upper_left': (300, 400), 'lower_right': (800, 850)},
    'Laptop_Sam': {'upper_left': (415, 415), 'lower_right': (950, 880)}
}

# Initialize game controller
game = GameController(website_url, template_path='images/sound_off_button.png')

# Open the game and turn off sound
game.open_game()
game.click_image()

# Digit recognition setup
digit_coords = [((1000, 600), (1025, 625)), ((1025, 600), (1055, 625)),
                ((1055, 600), (1083, 625)), ((1083, 600), (1110, 625)),
                ((1110, 600), (1136, 625)), ((1136, 600), (1165, 625))]
templates = {str(i): f'images/digit_templates/template_{i}.png' for i in range(10)}

recognizer = MultiDigitRecognizer(templates, image_path='images/screenshot.png')

# Loop to alternate between taking screenshots, recognizing numbers, and random clicking
for _ in range(100):  # Example: perform 100 iterations
    time.sleep(1.5)  # Wait for game state to stabilize

    # Take a screenshot
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save('images/screenshot.png')
    except Exception as e:
        print("Error saving screenshot:", e)
        break

    # Recognize the number from the screenshot
    number = recognizer.classify_digits(digit_coords, confidence_threshold=0.01)
    print("Recognized Number:", number)

    time.sleep(1)
    # Perform a random click in the game
    game.random_click_in_game()

    # Wait before next iteration
    time.sleep(1)



