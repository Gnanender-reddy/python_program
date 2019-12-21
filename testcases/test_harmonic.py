import unittest
from com.bridgelabz.FunctionalPrograms import Utility
from com.bridgelabz.FunctionalPrograms.Utility import harmonic


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(2.592857143,harmonic(7))


if __name__ == '__main__':
    unittest.main()
