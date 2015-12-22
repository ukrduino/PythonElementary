# Write a couple of unit tests for Exercise 4-1.

import unittest
from Lesson03.Exercise3_1_modified import string_sorter


class Test(unittest.TestCase):
    def setUp(self):
        self.rand_str = "mamamilaramu"
        self.char_dict = {'m': 4, 'a': 4, 'i': 1, 'l': 1, 'r': 1, 'u': 1}
        self.wrong_char_dict = {'m': 3, 'a': 4, 'i': 1, 'l': 1, 'r': 1, 'u': 1}

    def test_string_sorter_01(self):
        self.assertDictEqual(string_sorter(self.rand_str),
                             self.char_dict,
                             "Calculated number of each character in "
                             "rand_str should be equal to "
                             "number of characters in char_dict")

    def test_string_sorter_02(self):
        self.assertFalse(string_sorter(self.rand_str) == self.wrong_char_dict,
                         "Calculated number of each character "
                         "in rand_str should not be equal to "
                         "number of characters in wrong_char_dict")


if __name__ == "__main__":
    unittest.main()
