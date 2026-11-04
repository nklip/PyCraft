# LeetCode 1652: Defuse the Bomb
# https://leetcode.com/problems/defuse-the-bomb/description/
# Task: Decrypt the circular list code using the original values for every sum.
# For positive k, sum the next k entries; for negative k, sum the previous |k|.
# Exclude the current entry and wrap around either end as needed. For k = 0,
# use zeros. Return a new list containing the decrypted values.
class Solution:
    # Time Complexity: O(n + |k|), initializing and sliding the sum; O(n)
    # under the problem constraint |k| < n. For k = 0, filling zeros takes O(n).
    # Space Complexity: O(n) for the returned list; O(1) auxiliary space.
    # n = len(code), |k| = number of neighboring entries included in each sum.
    def decrypt(self, code: list[int], k: int) -> list[int]:
        if k == 0:
            return [0] * len(code)
        elif k < 0:
            return self.negativeEncoding(code, k)
        else:
            return self.positiveDecoding(code, k)

    def negativeEncoding(self, code: list[int], k: int) -> list[int]:
        decrypted = [0] * len(code)

        module = abs(k)

        sum = 0

        for i in range(-module, len(code), +1):
            value = (
                code[len(code) - abs(i)]
                if i < 0
                else code[i]
            )

            if i >= 0:
                decrypted[i] = sum

                sum += value

                value = (
                    code[len(code) - module + i]
                    if i - module < 0
                    else code[i - module]
                )

                sum -= value
            else:
                sum += value

        return decrypted

    def positiveDecoding(self, code: list[int], k: int) -> list[int]:
        decrypted = [0] * len(code)

        sum = 0

        for i in range(len(code) - 1 + k, -1, -1):
            value = (
                code[abs(i) - len(code)]
                if i > len(code) - 1
                else code[i]
            )
            if i <= len(code) - 1:
                decrypted[i] = sum

                sum += value

                value = (
                    code[i + k - len(code)]
                    if i + k > len(code) - 1
                    else code[i + k]
                )

                sum -= value
            else:
                sum += value

        return decrypted
