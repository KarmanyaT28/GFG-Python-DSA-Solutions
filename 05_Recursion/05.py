'''Count Digits in a Number
Difficulty: EasyAccuracy: 42.13%Submissions: 97K+Points: 2
You are given a number n. You need to find the count of digits in n.

Examples :

Input: n = 1
Output: 1
Explanation: Number of digit in 1 is 1.
Input: n = 99999
Output: 5
Explanation: Number of digit in 99999 is 5
Constraints:
1 ≤ n ≤ 109

'''

class Solution:
    def countDigits(self, n):
        
        if n<10:
            return 1
        
        return 1+ self.countDigits(n//10)


