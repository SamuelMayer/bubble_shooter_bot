import pytesseract
from PIL import Image
import cv2
import numpy as np
import logging

class OCRClass:
    def __init__(self):
        """Initialize the OCR class without needing screen coordinates."""

    def preprocess_image(self, image):
        """Preprocess the image for OCR."""
        # Convert the image to grayscale
        gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
        # Apply thresholding, etc., if needed
        # ...
        return gray_image

    def extract_text(self, image_path):
        """Extract text from the given image using OCR."""
        # Load the image from the given path
        image = Image.open(image_path)
        processed_image = self.preprocess_image(image)
        text = pytesseract.image_to_string(processed_image)
        return text


class ScoreProcessor:
    def __init__(self):
        """Initialize the ScoreProcessor class."""
    
    @staticmethod
    def clean_and_convert_score(text):
        """Clean OCR output and convert to integer."""
        # Remove non-numeric characters
        cleaned_text = ''.join(filter(str.isdigit, text))
        
        # Check if cleaned text is empty or not convertible to an integer
        if cleaned_text == '':
            return None  # or return a default value like 0
        else:
            return int(cleaned_text)

# Example usage:
ocr = OCRClass()
extracted_text = ocr.extract_text('images/Selection_011.png')
print(extracted_text)

# Assuming 'extracted_text' is the raw OCR output
# Example problematic OCR output
score_processor = ScoreProcessor()
cleaned_score = score_processor.clean_and_convert_score(extracted_text)
if cleaned_score is not None:
    print(f"Cleaned Score: {cleaned_score}")
else:
    print("No valid score extracted.")
#

