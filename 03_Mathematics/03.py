'''Given a positive integer n. You have to find factorial of n.

Examples:

Input: n = 4
Output: 24
Explanation: 4! = 4 * 3 * 2 * 1 = 24
Input: n = 11
Output: 39916800
Explanation: 11! = 11 * 10 * .. * 1 = 39916800
Constraints:
  0 ≤ n ≤ 11

'''

# Recursive Approach

def factorial(self,n):
    if n==0 or n==1:
        return 1
    return n * self.factorial(n-1)


# Iterative Approach

def factoriala(n):
    fact=1
    while n>0:
        fact = fact*n
        n = n-1

    return fact

n=5
print(factoriala(n))