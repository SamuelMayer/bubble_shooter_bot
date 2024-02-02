import cv2
import numpy as np

class MultiDigitRecognizer:
    def __init__(self, templates, image_path):
        self.templates = {digit: cv2.imread(path, 0) for digit, path in templates.items()}
        self.image_path = image_path
        self.game_image = self.load_image(image_path)

    def load_image(self, path):
        image = cv2.imread(path, 0)
        if image is None:
            print(f"Error loading image from {path}")
        return image


    def recognize_digit(self, image, digit_template):
        res = cv2.matchTemplate(image, digit_template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(res)
        return max_val

    def classify_digits(self, digit_coords, confidence_threshold):
        recognized_number = ''
        if self.game_image is not None:
            for coords in digit_coords:
                digit_roi = self.game_image[coords[0][1]:coords[1][1], coords[0][0]:coords[1][0]]
                digit_scores = {digit: self.recognize_digit(digit_roi, template) for digit, template in self.templates.items()}
                best_match = max(digit_scores, key=digit_scores.get)
                confidence = digit_scores[best_match]
                if confidence >= confidence_threshold:
                    recognized_number += best_match
                else:
                    recognized_number += '?'  # or any other symbol for low-confidence recognition
        return recognized_number



# Usage
#templates = {
#    '0': 'images/digit_templates/template_0.png',
#    '1': 'images/digit_templates/template_1.png',
#    '2': 'images/digit_templates/template_2.png',
#    '3': 'images/digit_templates/template_3.png',
#    '4': 'images/digit_templates/template_4.png',
#    '5': 'images/digit_templates/template_5.png',
#    '6': 'images/digit_templates/template_6.png',
#    '7': 'images/digit_templates/template_7.png',
#    '8': 'images/digit_templates/template_8.png',
#    '9': 'images/digit_templates/template_9.png'
#}

#templates = {str(i): f'images/digit_templates/template_{i}.png' for i in range(10)}
#
#digit_coords = [((1000, 600), (1025, 625)), ((1025, 600), (1055, 625)), ((1055, 600), (1083, 625)), ((1083, 600), (1110, 625)), ((1110, 600), (1136, 625)), ((1136, 600), (1165, 625))]  # List of tuples of top-left and bottom-right coords for each digit
#image_path = 'images/screenshot.png'
#recognizer = MultiDigitRecognizer(templates, image_path)
#number = recognizer.classify_digits(digit_coords, 0.1)
#print("Recognized Number:", number)