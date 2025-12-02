import unittest
from puzzle1 import FindRangeOfSplitableNumbers

class TestFindRangeOfSplitableNumbers(unittest.TestCase):
    def test1(self):
        start, end = FindRangeOfSplitableNumbers("345", "5678")
        self.assertEqual(start, 1000)
        self.assertEqual(end, 5678)

    def test2(self):
        start, end = FindRangeOfSplitableNumbers("345", "567")
        self.assertEqual(start, 0)
        self.assertEqual(end, 0)

    def test3(self):
        start, end = FindRangeOfSplitableNumbers("1", "999")
        self.assertEqual(start, 10)
        self.assertEqual(end, 99)

if __name__ == "__main__":
    unittest.main()