from whiteboard import solution
from unittest import TestCase, main


class PossiblePalindromeChecker(TestCase):

    def test_empty_list(self):
        self.assertTrue(solution("aabbcc"))

    def test_one_double(self):
        self.assertTrue(solution("aabebcc"))

    def test_multiple_doubles(self):
        self.assertTrue(solution("racecar"))

    def test_odd_numbers(self):
        self.assertFalse(solution("abcd"))

    def test_no_double_odd_numbers(self):
        self.assertFalse(solution("aaabbbcc"))

if __name__ == '__main__':
    main()