import numpy as np
from .writer import Writer

class Display:
    def __init__(self, writer, shape=(8,8)):
        if shape[0] < 1 or shape[1] < 1:
            raise ValueError("The elements of shape must all be positive")

        self.shape = shape
        self.writer = writer

    def draw(self, image : np.ndarray):
        """
        Draws an image to the display. Will truncate extra data from the image array.
        :param image: Array with the binary image data.
        :type image: numpy.ndarray
        """
        if not isinstance(image, np.ndarray):
            raise ValueError("The image to display must be a numpy array")

        # vertical size
        if image.shape[0] < self.shape[0]:
            pass

