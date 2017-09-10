import numpy as np
from .writer import Writer
from copy import deepcopy

class Display:
    def __init__(self, writer, shape: tuple=(8, 8)):
        if shape[0] < 1 or shape[1] < 1:
            raise ValueError("The elements of shape must all be positive")

        self.shape = shape
        self.writer = writer

    def draw(self, image: np.ndarray):
        """
        Draws an image to the display. Will truncate extra data from the image array.
        :param image: Array with the binary image data.
        :type image: numpy.ndarray
        """
        if not isinstance(image, np.ndarray):
            raise ValueError("The image to display must be a numpy array")

        image = Display._truncate_size(image, self.shape)
        image_flat = image.flatten('C')
        self.writer.write(image_flat)


    @staticmethod
    def _truncate_size(image: np.ndarray, shape: tuple) -> np.ndarray:
        out = deepcopy(image)

        # vertical size
        vd = out.shape[0] - shape[0]
        if vd > 0:
            out = out[0:8][:]
        elif vd < 0:
            out = np.vstack((out, np.zeros(vd, out.shape[1])))

        # horizontal size
        hd = out.shape[1] - shape[1]
        if hd > 0:
            out = out[:][0:8]
        elif hd < 0:
            out = np.hstack((out, np.zeros(out.shape[0], hd)))

        return out
