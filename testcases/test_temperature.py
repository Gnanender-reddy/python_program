import unittest

from com.bridgelabz.FunctionalPrograms.Utility import TemperatureConversion


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(35.6, TemperatureConversion(2))


if __name__ == '__main__':
    unittest.main()
