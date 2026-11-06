import unittest

from algs.easy.guess_number_higher_or_lower import Solution


class TestGuessNumberHigherOrLower(unittest.TestCase):
    def test_pick_six_among_ten_numbers(self):
        self.assertEqual(Solution(6).guessNumber(10), 6)

    def test_only_number_is_picked(self):
        self.assertEqual(Solution(1).guessNumber(1), 1)

    def test_pick_one_among_two_numbers(self):
        self.assertEqual(Solution(1).guessNumber(2), 1)


if __name__ == "__main__":
    unittest.main()
