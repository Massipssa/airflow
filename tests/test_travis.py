import unittest
from src.main import string_comma_to_list


class BasicsTest(unittest.TestCase):
    
    def test_select_all(self):
        self.assertEqual(1, 1)

    def test_string_comma_to_list(self):
        msg1 = "one, two, three"
        msg2 = ""
        self.assertEqual(len(string_comma_to_list(msg1)), 3)
        self.assertEqual(len(string_comma_to_list(msg2)), 0)