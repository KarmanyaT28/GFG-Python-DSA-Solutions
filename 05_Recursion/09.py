'''Recursively Sum N Numbers
Difficulty: EasyAccuracy: 58.43%Submissions: 17K+Points: 2Average Time: 15m
You are given a number n. You need to recursively sum the numbers from 1 to n and return the sum.

Example 1:

Input:
n = 5
Output: 15
Example 2:

Input:
n = 4
Output: 10
Your Task:

Complete the function recursiveSum that takes n as paramenter and return the sum.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N) (Recursive).

Constraints:
0 <= n <= 100

'''

#User function Template for python3

class Solution:
    def recursiveSum(self,n):
        if n==0:
            return 0
            
        elif n==1:
            return 1
            
        sum=n+self.recursiveSum(n-1)
        
        return sum