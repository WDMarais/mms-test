import unittest

def params_are_valid(a, x, N):
    # If array is empty, it can't contain x or any smaller elements
    if N == 0:
        return False

    # Design choice - spec stated list was sorted, algorithm uses this fact, so if
    # the list is not sorted, also return error. Alternatively, list could be sorted, but that
    # would add n log n processing time, whereas the check and error adds n processing time in the worst case.
    if not is_sorted(a):
        return False
    return True

def is_sorted(l):
    return all(a <= b for a, b in zip(l, l[1:]))

def f(a, x):
    N = len(a)
    # Check basic stuff, like
    # - Whether the list contains elements at all
    # - Whether the list is sorted
    if not params_are_valid(a, x, N):
        return -1

class TestFunction(unittest.TestCase):
    def test_empty_array(self):
        actual = f([], 1)
        expected = -1
        self.assertEqual(actual, expected)

    def test_unsorted_array(self):
        actual = f([1, 3, 2], 1)
        expected = -1
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
