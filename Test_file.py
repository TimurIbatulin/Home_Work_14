import unittest
from For_test import file_info

class TestForTestWork(unittest.TestCase):
    def test_method(self):
        self.assertEqual(file_info('/Users/timuribatulin/Downloads/images.png'), ('/Users/timuribatulin/Downloads/images.png', 'images.png', 'png'))

if __name__ =='__main__':
    unittest.main()