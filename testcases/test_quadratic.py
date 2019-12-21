import unittest

from com.bridgelabz.FunctionalPrograms.Utility import quadratic


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual((-1-1.4142135623730951j) (-1+1.4142135623730951j), quadratic(1,2,3))


if __name__ == '__main__':
    unittest.main()
