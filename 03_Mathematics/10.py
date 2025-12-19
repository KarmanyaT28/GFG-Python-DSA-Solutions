'''Multiplication Under Modulo
Difficulty: BasicAccuracy: 83.95%Submissions: 38K+Points: 1
Given three integers a, b, and M, your task is to compute the result of the modular multiplication operation: (a×b) % M
This operation returns the remainder when the product of a and b is divided by M. The result will always be an integer between 0 and M-1.

Examples:

Input: a = 5, b = 3, M = 11
Output: 4
Explanation: a × b = 5 × 3 = 15, 15 % 11 = 4, so the result is 4.
Input: a = 12, b = 15, M = 7
Output: 5
Explanation: a × b = 12 × 15 = 180, 180 % 7 = 5, so the result is 5.
Constraints:
1 ≤ a, b ≤ 104
2 ≤ M ≤ 109

'''


class Solution:
    def modmul(self, a, b, M):
        prod = a*b
        return prod%M
        