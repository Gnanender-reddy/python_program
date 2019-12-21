import unittest

from com.bridgelabz.FunctionalPrograms.Utility import calculateDistance


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1.4142135623730951, calculateDistance(1,2,3,4))


if __name__ == '__main__':
    unittest.main()
