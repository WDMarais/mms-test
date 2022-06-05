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

    # If first (and since sorted, smallest) element is larger than x,
    # the list contains no elements smaller than x
    if a[0] > x:
        return -1

    c = N - 1
    while c > 0: # 0 was checked first
        el = a[c]
        if el <= x:
            return el
        c -= 1

class TestFunction(unittest.TestCase):
    # Could potentially use some dict structure to keep this array and its
    # tests specifically grouped together. I opted to go for the simpler choice of
    # just keeping them separate.
    example_arr = [ 3, 4, 6, 9, 10, 12, 14, 15, 17, 19, 21 ]
    def test_example_arr_equal(self):
        actual = f(self.example_arr, 10)
        expected = 10
        self.assertEqual(actual, expected)

    def test_example_arr_smaller(self):
        actual = f(self.example_arr, 16)
        expected = 15

    def test_list_all_smaller(self):
        actual = f([1, 2, 3, 4], 5)
        expected = 4
        self.assertEqual(actual, expected)

    def test_list_all_larger(self):
        actual = f([2, 3, 4], 1)
        expected = -1
        self.assertEqual(actual, expected)

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
