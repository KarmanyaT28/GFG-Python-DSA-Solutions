'''Fibonacci Using Recursion
Difficulty: BasicAccuracy: 78.37%Submissions: 71K+Points: 1
You are given a number n. You need to find the nth Fibonacci number.

Note: F(n) = F(n-1) + F(n-2) ; where F(0) = 0 and F(1) = 1

Example:

Input: n = 3
Output: 2
Explanation: The Fibonacci sequence starts as 0, 1, 1, 2, 3, 5... The 3rd Fibonacci number is 2.
Input: n = 5
Output: 5
Explanation: The sequence is 0, 1, 1, 2, 3, 5... The 5th Fibonacci number is 5.
Constraints:
1 ≤ n ≤ 20

'''


class Solution:
    def nthFibonacci(self, n):
        if n==0:
            return 0
        elif n==1:
            return 1
            
        else:
            return self.nthFibonacci(n-1) + self.nthFibonacci(n-2)