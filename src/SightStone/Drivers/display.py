import numpy as np
from .writer import Writer

class Display:
    def __init__(self, writer, shape=(8,8)):
        self.writer = writer

    def draw(self):
