'''Factorial Using Recursion
Difficulty: EasyAccuracy: 63.18%Submissions: 17K+Points: 2Average Time: 10m
You are given a number n. You need to recursively find the factorial of n and return it.

Example 1:

Input:
n = 5
Output: 120
Example 2:

Input:
n = 0
Output: 1
Your Task:

Complete the function factorial that takes n as parameter and returns the factorial. 

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N) (Recursive).

Constraints:
0 <= n <= 10

'''

#User function Template for python3

class Solution:
    def factorial(self,n):
        if n==0:
            return 1
        elif n==1:
            return 1
        else:
            return n * self.factorial(n-1)
