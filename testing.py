import unittest
import helloworld

class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(helloworld.testing('a'), 'a')

if __name__ == '__main__':
    unittest.main()
