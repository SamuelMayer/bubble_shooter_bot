import sqlite3
import cv2
import numpy as np
import time
from datetime import datetime
from PIL import Image

class GameStateStorage:
    def __init__(self, db_path):
        """Initialize the database connection."""
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        """Create a table for storing game states if it doesn't exist."""
        create_table_sql = '''
        CREATE TABLE IF NOT EXISTS game_states (
            id INTEGER PRIMARY KEY,
            image BLOB NOT NULL,
            score INTEGER NOT NULL,
            timestamp TEXT NOT NULL
        );
        '''
        c = self.conn.cursor()
        c.execute(create_table_sql)
        self.conn.commit()

    def insert_game_state(self, image_path, score):
        """Insert a new game state into the database."""
        # Convert the image to binary format
        image = self.convert_image_to_binary(image_path)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        insert_sql = '''INSERT INTO game_states (image, score, timestamp) VALUES (?, ?, ?)'''
        c = self.conn.cursor()
        c.execute(insert_sql, (image, score, timestamp))
        self.conn.commit()

    def convert_image_to_binary(self, image_path):
        """Convert an image file to binary data."""
        with open(image_path, 'rb') as file:
            blob = file.read()
        return blob

    def close(self):
        """Close the database connection."""
        self.conn.close()

# Example usage
## Create an instance of the class and insert a game state
#db_path = 'game_data.db'
#game_storage = GameStateStorage(db_path)
#
## Assuming 'extracted_text' contains the score from the OCR process in main.py
## And 'images/screenshot.png' is the path to the screenshot image
#extracted_text = '100'  # Example score
#image_path = 'images/screenshot.png'
#game_storage.insert_game_state(image_path, int(extracted_text))
#
## Don't forget to close the database connection when done
#game_storage.close()


