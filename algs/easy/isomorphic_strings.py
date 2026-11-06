# LeetCode 205: Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/description/
# Task: Check whether equal-length strings s and t match under a consistent
# one-to-one character substitution. Preserve character order, allow self-maps,
# and prevent two different source characters from sharing a target character.
class Solution:
    # Time Complexity: O(n) average, checking each pair with dictionary/set lookups.
    # Space Complexity: O(u), for the mapping and the set of used target characters.
    # n = len(s) = len(t), u = number of distinct source characters stored, u <= n.
    # Hash operations average O(1); the fixed ASCII alphabet bounds space to O(1).
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict = {}
        busy = set()

        for i in range (len(s)):
            ch1 = s[i]
            ch2 = t[i]

            if ch1 not in dict and ch2 not in busy:
                dict[ch1] = ch2
                busy.add(ch2)
            elif ch1 not in dict and ch2 in busy:
                return False
            elif ch2 != dict.get(ch1):
                return False

        return True
