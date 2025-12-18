'''Convert Celsius To Fahrenheit
Difficulty: BasicAccuracy: 82.57%Submissions: 74K+Points: 1
Given a temperature in celsius C. You need to convert the given temperature into Fahrenheit.

Examples:

Input: C = 32
Output: 89.6
Explanation: Using the conversion formula of celsius to farhenheit , it can be calculated that, for 32 degree celsius, the temperature in Fahrenheit = 89.6
Input: C = 50
Output: 122
Explanation: Using the conversion formula of celsius to farhenheit, it can be calculated that, for 50 degree C, the temperature in Fahrenheit = 122.
Constraints:
1 ≤ C ≤ 104

The formula to convert celsius to fahrenheit is: (C * 9/5) + 32'''

class Solution:
    def cToF(self,C):
        F = (C*9/5)+32
        return F
