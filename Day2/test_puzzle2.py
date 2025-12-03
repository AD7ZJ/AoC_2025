import unittest
from puzzle2 import FindRangeOfSplitableNumbers
from puzzle2 import CheckForPatternsOfLengthN

class TestFindRangeOfSplitableNumbers(unittest.TestCase):
    def test1(self):
        start, end = FindRangeOfSplitableNumbers("345", "5678", 2)
        self.assertEqual(start, 1000)
        self.assertEqual(end, 5678)

    def test2(self):
        start, end = FindRangeOfSplitableNumbers("345", "567", 2)
        self.assertEqual(start, 0)
        self.assertEqual(end, 0)

    def test3(self):
        start, end = FindRangeOfSplitableNumbers("1", "999", 2)
        self.assertEqual(start, 10)
        self.assertEqual(end, 99)

    def test3(self):
        start, end = FindRangeOfSplitableNumbers("1", "999", 3)
        self.assertEqual(start, 100)
        self.assertEqual(end, 999)

    def test4(self):
        start, end = FindRangeOfSplitableNumbers("1", "12345", 3)
        self.assertEqual(start, 100)
        self.assertEqual(end, 999)

    def test5(self):
        start, end = FindRangeOfSplitableNumbers("1", "1234567", 3)
        self.assertEqual(start, 100)
        self.assertEqual(end, 999999)

    def test6(self):
        start, end = FindRangeOfSplitableNumbers("1", "1234567", 5)
        self.assertEqual(start, 10000)
        self.assertEqual(end, 99999)

class TestCheckForPatterns(unittest.TestCase):
    def test1(self):
        patterns = CheckForPatternsOfLengthN(10, 99, 2)
        self.assertEqual(patterns, [11, 22, 33, 44, 55, 66, 77, 88, 99 ])

    def test2(self):
        patterns = CheckForPatternsOfLengthN(100, 245, 3)
        self.assertEqual(patterns, [111, 222 ])

    def test3(self):
        patterns = CheckForPatternsOfLengthN(100000, 101101, 3)
        self.assertEqual(patterns, [101010])

    def test4(self):
        patterns = CheckForPatternsOfLengthN(100000, 120000, 6)
        self.assertEqual(patterns, [111111])
        
if __name__ == "__main__":
    unittest.main()