import cv2
import numpy as np
from math import ceil

class ASCIIEngine:
    """ASCII engine
    
    It represents your original image to ASCII text in several steps:
    
        1. Original image converts to gray format
        2. Calculating 8*8 block sums (because default size of ASCII symbol is 8 pix (P.S it can be different for different font-size))
        3. Basing on sums, engine choose the ascii symbol from "steps"
    """
    
    steps = [' ', '.', ',', ':', ';', '+', '*', 'o', 'O', 'S', '8', '#', '%', '@']
    
    
    def __init__(self):
        """Initialization ASCIIEngine and calculating step_divite to choose ascii symbols
        """
        self.step_divide = ceil(8 * 8 * 255 / len(self.steps))
        
    
    def _make_gray_scale(self, frame: np.ndarray) -> np.ndarray:
        """This function converts original color image to grayscale format
        Additionally it "cleans" tresholds (30 and 240)

        Args:
            frame (np.ndarray): input image in numpy representation

        Returns:
            np.ndarray: output grayscale image in numpy representation
        """
        grayscale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        grayscale_image = np.where(grayscale_image >= 30, grayscale_image, 0)
        grayscale_image = np.where(grayscale_image <= 240, grayscale_image, 255)
        return grayscale_image

    def _process_image_in_chunks(self, image: np.ndarray) -> np.ndarray:
        """This function calculates scores for 8 * 8 pixels blocks
        
        Original 2D image (H, W) reshapes to 4D tensor (H // 8, 8, W // 8, 8)
        and then function calculates sums by axis 1 and 3.
        Result of this operations is an array scores for each 8 * 8 blocks
        

        Args:
            image (np.ndarray): grayscale image in numpy format

        Returns:
            np.ndarray: array of blocks scores
        """
        h, w = image.shape
        block_sums = image.reshape(h // 8, 8, w // 8, 8).sum(axis=(1, 3))
        
        # Subtract 1 from all non-zero block sums to normalize scores and avoid potential division errors
        block_sums -= np.where(block_sums > 0, 1, 0).astype(block_sums.dtype)
        return block_sums
    
    def get_ascii(self, frame: np.ndarray, new_size: None | tuple=None) -> str:
        """Main engine function which provides API to create ASCII text from image

        Args:
            frame (np.ndarray): original image in numpy format
            new_size (None | tuple, optional): new size for image (if None, the size is image.shape). Defaults to None.

        Returns:
            str: ASCII text
        """
        height, width = new_size if new_size else frame.shape[:2]
        
        height += 8 - (height % 8)
        width += 8 - (width % 8)

        image = cv2.resize(frame, (width * 2, height), interpolation=cv2.INTER_LINEAR)
        image = self._make_gray_scale(image)

        block_sums = self._process_image_in_chunks(image)
        ascii_art = [
            ''.join(self.steps[score // self.step_divide] for score in row)
            for row in block_sums
        ]
        
        return "\n".join(ascii_art)