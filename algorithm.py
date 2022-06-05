import unittest

def f(a, x):
    N = len(a)
    if N == 0:
        return -1

class TestFunction(unittest.TestCase):
    def test_empty_array(self):
        actual = f([], 1)
        expected = -1
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
