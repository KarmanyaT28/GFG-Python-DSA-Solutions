'''Given a number n , check if it is prime or not.
Note :  A prime number is a number which is only divisible by 1 and itself.

Examples :

Input: n = 5
Output: true
Explanation: 5 is only divisible by 1 and itself. So, 5 is a prime number.
Input: n = 4
Output: false
Explanation: 4 is divisible by 2.So, 4 is not a prime number.
Constraints:
  1 ≤ n ≤ 109'''


def isPrime(n):
    if n==1:
        return False
    elif n==2:
        return True
    else:
        p=2
        while((p*p)<=n):
            if n%p==0:
                return False
            p+=1
    return True


n=29
print(isPrime(n))
    