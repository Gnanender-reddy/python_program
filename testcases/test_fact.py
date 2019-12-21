import unittest

from com.bridgelabz.FunctionalPrograms.Utility import factorial


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(120, factorial(5))


if __name__ == '__main__':
    unittest.main()
