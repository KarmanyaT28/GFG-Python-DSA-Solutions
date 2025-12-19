'''Addition Under Modulo
Difficulty: BasicAccuracy: 65.19%Submissions: 64K+Points: 1Average Time: 10m
Given three integers a, b, and M, your task is to compute the result of the modular addition operation:
Note: Modular operations returns the remainder when divided by M. The result will always be an integer between 0 and M−1.

Examples :

Input: a = 10, b = 20, M = 3
Output: 0
Explanation: (10 + 20) mod 3 = 0
Input: a = 100, b = 13, M = 107
Output: 6
Explanation: (100 + 13) mod 107 = 6
Constraints:'''


class Solution:
    def sumUnderModulo(self, a, b, M):
        sum = a+b
        return sum%M