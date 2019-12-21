import unittest

from com.bridgelabz.Oops.companylist.company import Company


class MyTestCase(unittest.TestCase):
    def test_adding_list(self):
        com=Company()
        com.adding_list()
        #self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
