import unittest

from sightstone import drivers

from time import sleep
import numpy as np


class TestWriter(unittest.TestCase):
    def test_led(self):
        with drivers.Writer(DAT_A=14, DAT_B=15, CLK=18) as writer:
            data = [1, 0, 1, 0, 1, 0, 1, 0]
            writer.write(data)

            sleep(5)

            data = True
            for _ in range(0, 80):
                writer.write_one(data)
                data = not data
                sleep(0.5)


class TestDisplayTruncate(unittest.TestCase):
    def setUp(self):
        self.a = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])

    def test_truncate_stay(self):
        b = drivers.Display._truncate_size(self.a, (3,3))
        self.assertTrue(self.a == b)

    def test_truncate_bigger(self):
        b = drivers.Display._truncate_size(self.a, (4,4))
        c = np.array([[1, 2, 3, 0],
                      [4, 5, 6, 0],
                      [7, 8, 9, 0],
                      [0, 0, 0, 0]])
        self.assertTrue(b == c)

    def test_truncate_smaller(self):
        b = drivers.Display._truncate_size(self.a, (4, 4))
        c = np.array([[1, 2],
                      [4, 5]])
        self.assertTrue(b == c)