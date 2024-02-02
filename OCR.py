import pytesseract
from PIL import ImageGrab
import cv2
import numpy as np
import logging

class OCRClass:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def capture_area(self):
        """Capture the specified screen area."""
        return ImageGrab.grab(bbox=(self.top_left[0], self.top_left[1], self.bottom_right[0], self.bottom_right[1]))

    def preprocess_image(self, image):
        """Preprocess the image for OCR."""
        # Convert the image to grayscale
        gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
        # Write image for debgging DELETE!
        cv2.imwrite('images/debug_preprocessed.png', gray_image)
        # Apply thresholding, etc. if needed
        # ...
        return gray_image

    def extract_text(self, image):
        """Extract text from the given image using OCR."""
        processed_image = self.preprocess_image(image)
        text = pytesseract.image_to_string(processed_image)
        return text

# Example usage
# Define the top left and bottom right coordinates of the score area
# x1 = 1015
# y1 = 595
# x2 = 1161
# y2 = 622
# top_left = (1015, 595)
# bottom_right = (x2, y2)
# ocr = OCRClass(top_left, bottom_right)
# screenshot = ocr.capture_area()
# extracted_text = ocr.extract_text(screenshot)
# print(extracted_text)
