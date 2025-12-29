'''Find nCr
Difficulty: EasyAccuracy: 52.44%Submissions: 15K+Points: 2Average Time: 15m
You are given two numbers n and r. You need to find nCr.
nCr = (n!) / ((n-r)!*(r!))
In recursive way, we can write nCr as nCr = (n-1)C(r-1) + (n-1)Cr

Example 1:

Input:
n = 5, r = 2
Output: 10
Example 2:

Input:
n = 4, r = 1
Output: 4
Your Task:
You only need to complete the function nCr that takes n and r as parameters and returns the nCr.

Expected Time Complexity: O(2N).
Expected Auxiliary Space: O(2N) (Recursive).

Constraints:
1 <= r <= n <= 30

'''


#User function Template for python3


def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n * factorial(n-1)



def nCr(n,r):
    if r>n:
        return 0
    val = factorial(n)//(factorial(n-r)*factorial(r))
    return val
    