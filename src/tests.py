import unittest

from sightstone import drivers

from time import sleep
import numpy as np

DAT_A = 8
DAT_B = 10
CLK = 12
CLR = 3

class TestWriter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.writer = drivers.Writer(DAT=8, CLK=10, CLR=12)
        cls.writer.open()
    
    @classmethod
    def tearDownClass(cls):
        cls.writer.close()

    def tearDown(self):
        sleep(1) # sleep one second between tests

    def led_write_one_one(self):
        self.writer.write_one(1)

    def led_write_one_alternate(self):
        data = True
        for _ in range(0, 999999999):
            self.writer.write_one(data)
            data = not data
            sleep(0.1)

    def led_write_one_all(self):
        data = True
        for _ in range(0, 8):
            self.writer.write_one(data)
            sleep(0.5)

    def led_write_last(self):
        data = [0, 0, 0, 0, 0, 0, 0, 1]
        self.writer.write(data)

    def led_write(self):
        data = [1, 0, 1, 0, 1, 0, 1, 0]
        self.writer.write(data)

    def led_clear(self):
        self.writer.write([1,1,1,1,1,1,1,1])
        sleep(0.5)
        self.writer.clear()


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