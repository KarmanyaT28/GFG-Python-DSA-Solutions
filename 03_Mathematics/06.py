'''# Exactly 3 Divisors

Given a positive integer value n. The task is to find how many numbers less than or equal to n have numbers of divisors exactly 3.

Examples:

Input: n = 6
Output: 1
Explanation: The only number less than 6 with 3 divisors is 4 which has 1, 2 and 4 as divisors.
Input: n = 10
Output: 2
Explanation: 4 and 9 have 3 divisors.'''


def isPrime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def exactly3Divisors(n):
    count=0
    for i in range(2,int(n**0.5)+1):
        if isPrime(i):
            count+=1
    return count