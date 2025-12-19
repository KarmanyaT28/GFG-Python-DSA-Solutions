'''Modular Inverse
Difficulty: EasyAccuracy: 43.0%Submissions: 89K+Points: 2
Given two integers n and m. You have to find the smallest modular multiplicative inverse of n under modulo m. if it does not exist then return -1.

Examples :

Input: n = 3, m = 11
Output: 4
Explanation: Since (4 × 3) mod 11 = 1, 4 is the modulo inverse of 3 under mod 11.
Input: n = 10, m = 17
Output: 12
Explanation: Since (12*10) mod 17 = 1, 12 is the modulo inverse of 10.'''


class Solution:    
    def modInverse(self,n,m):
        for i in range(1,m+1):
            if (n*i)%m==1:
                return i
            else:
                i=i+1
                
        return -1
            