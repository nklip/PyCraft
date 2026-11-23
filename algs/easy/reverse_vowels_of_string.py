# LeetCode 345: Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
# Task: Return a string with its vowels in reverse order, leaving all other
# characters at their original positions. Treat a, e, i, o, and u in either
# case as vowels, preserving each vowel's case when moving it.
class Solution:
    # Time Complexity: O(n), building the list, scanning inward, and joining it.
    # Space Complexity: O(n), for the character list and returned string.
    # n = len(s); the set of ten vowel characters uses O(1) space.
    def reverseVowels(self, s: str) -> str:
        vowels = self.getVowels()

        left = 0
        right = len(s) - 1

        array = list(s)

        while left < right:
            ch_left = array[left]
            ch_right = array[right]

            if ch_left in vowels and ch_right in vowels:
                array[left] = ch_right
                array[right] = ch_left

                left += 1
                right -= 1
            elif ch_left not in vowels:
                left += 1
            elif ch_right not in vowels:
                right -= 1

        return "".join(array)

    def getVowels(self) -> set:
        vowels = set()

        vowels.add('a')
        vowels.add('e')
        vowels.add('i')
        vowels.add('o')
        vowels.add('u')
        vowels.add('A')
        vowels.add('E')
        vowels.add('I')
        vowels.add('O')
        vowels.add('U')
        return vowels
