'''GCD Euclid
Difficulty: BasicAccuracy: 66.46%Submissions: 12K+Points: 1Average Time: 15m
You are given two numbers a and b. Find their GCD using recursion.

Example 1:

Input:
a = 7, b = 8
Output: 1
Example 2:

Input:
a = 2, b = 4
Output: 2
Your Task:

Complete the function GCD that takes a and b as parameters and returns the GCD.

Constraints:
1 <= a, b <= 100

'''

class Solution:
    def GCD(self, a, b):
        # Base Case: If b becomes 0, the GCD is a
        if b == 0:
            return a
        
        # Recursive Step: 
        # Call GCD again, making 'b' the new 'a' 
        # and 'a % b' the new 'b'
        return self.GCD(b, a % b)
    

