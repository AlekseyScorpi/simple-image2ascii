import cv2
import numpy as np
import unittest
from image2ascii import ASCIIEngine

class TestASCIIEngine(unittest.TestCase):
    def setUp(self):
        self.engine = ASCIIEngine()
    
    def test_ascii_output_not_empty(self):
        image = np.ones((64, 128, 3), dtype=np.uint8) * 255  # Белое изображение
        ascii_art = self.engine.get_ascii(image)
        self.assertTrue(len(ascii_art) > 0, "ASCII output should not be empty")

    def test_ascii_characters_valid(self):
        image = np.ones((64, 128, 3), dtype=np.uint8) * 128  # Серое изображение
        ascii_art = self.engine.get_ascii(image)
        valid_chars = set(self.engine.steps)
        self.assertTrue(all(char in valid_chars or char == "\n" for char in ascii_art), "Invalid ASCII characters found")

if __name__ == "__main__":
    unittest.main()