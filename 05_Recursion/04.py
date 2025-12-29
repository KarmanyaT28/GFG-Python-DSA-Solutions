'''
Sum of Digits of a Number
Difficulty: BasicAccuracy: 73.02%Submissions: 74K+Points: 1
You are given a number n. You need to find the sum of digits of n.

Examples :

Input: n = 1
Output: 1
Explanation: Sum of digit of 1 is 1.
Input: n = 99999
Output: 45
Explanation: Sum of digit of 99999 is 45.
Constraints:
1 ≤ n ≤ 107

'''

class Solution:
    def sumOfDigits(self, n):
        if n==0:
            return 0
            
        num = n%10
        rem_num = n//10
        
        return num+self.sumOfDigits(rem_num)
        


