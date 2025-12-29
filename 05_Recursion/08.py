'''Check Palindrome
Difficulty: EasyAccuracy: 49.98%Submissions: 25K+Points: 2Average Time: 15m
You are given a number n. You need to see if the number is a palindrome or not (recursively)

Example 1:

Input:
n = 100
Output: 0
Example 2:

Input:
n = 101
Output: 1
Your Task:

Complete the function isPalin that takes n as parameter and returns true or false . (In case of true, 1 will be printed by the driver code, otherwise 0)

Expected Time Complexity: O(Log(N)).
Expected Auxiliary Space: O(Log(N)) (Recursive).

Constraints:
1 <= n <= 108

'''


def isPalin(self, n, rev=0, original=None):
        # On the first call, store the starting n to compare later
        if original is None:
            original = n
            
        # Base Case: All digits processed
        if n == 0:
            return rev == original
        
        # Recursive Step:
        # Build the reverse: (rev * 10) + last digit
        # Pass the original value down so we don't lose it
        return self.isPalin(n // 10, (rev * 10) + (n % 10), original)