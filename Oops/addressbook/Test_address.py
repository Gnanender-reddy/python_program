import unittest

import pytest

from com.bridgelabz.Oops.addressbook.addressbook import Addressbook


class MyTestCase(unittest.TestCase):
    def test_add_details(self):

        obj = Addressbook(self)
        with pytest.raises(TypeError):
            obj.add_details()
        self.assertEqual(True, False)
    # def test_delete_data(self):
    #
    #     obj = Addressbook(self)
    #     with pytest.raises(TypeError):
    #         obj.delete_data()
    # def test_update_details(self):
    #
    #     obj = Addressbook(self)
    #     with pytest.raises(TypeError):
    #         obj.update_details()


if __name__ == '__main__':
    unittest.main()
