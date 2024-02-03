import webbrowser
import subprocess
import pyautogui
import time
import random
import cv2
from GameController import GameController
from OCR import OCRClass, ScoreProcessor
from data_handling import GameStateStorage


# Define the website URL for Bubble Shooter
website_url = "https://www.bubbleshooter.de/spiele/bubble-shooter-klassisch"

# Pixel Vectors to adjust for different Monitors
click_areas = {
    'Samsung': {'upper_left': (570, 290), 'lower_right': (1125, 810)},
    'MacBook_Trisha': {'upper_left': (300, 400), 'lower_right': (800, 850)},
    'Laptop_Sam': {'upper_left': (570, 290), 'lower_right': (1125, 810)}
}

# Initialize game controller
game = GameController(website_url, click_area = click_areas['Laptop_Sam'])

# Open the game and turn off sound
game.open_game()
time.sleep(4)    


# scroll down  
pyautogui.click(1745, 270) # necessary to make window 'active'
pyautogui.scroll(-3)
time.sleep(1)

# Start game
game.click_image(template_path='images/start_game_button.png')
time.sleep(1)

# turn off sound
game.click_image(template_path='images/sound_off_button.png')

# Loop to alternate between taking screenshots, recognizing numbers, and random clicking
for _ in range(100):  # Example: perform 100 iterations
    time.sleep(1.5)  # Wait for game state to stabilize
  
    # Game state
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save('images/game_state.png')
    except Exception as e:
        print("Error saving game state screenshot:", e)
        break

    # Points
    # Take a screenshot 
    # Define the region to capture (left, top, width, height)
    region = (1187, 516, 150, 38)
    try:
        screenshot = pyautogui.screenshot(region=region)
        screenshot.save('images/points.png')
    except Exception as e:
        print("Error saving points screenshot:", e)
        break

    # Recognize the number from the screenshot
    ocr = OCRClass()
    extracted_text = ocr.extract_text('images/points.png')
    # Process score for storage in DB
    score_processor = ScoreProcessor()
    cleaned_score = score_processor.clean_and_convert_score(extracted_text)

    # Save Game State and points
    # Create an instance of the class and insert a game state
    db_path = 'game_data.db'
    game_storage = GameStateStorage(db_path)

    # Assuming 'extracted_text' contains the score from the OCR process in main.py
    # And 'images/game_state.png' is the path to the screenshot image
    image_path = 'images/game_state.png'   
    game_storage.insert_game_state(image_path, int(cleaned_score))
    # Don't forget to close the database connection when done
    game_storage.close()

    time.sleep(1)
    # Perform a random click in the game
    game.random_click_in_game()

    # Wait before next iteration
    time.sleep(1)




