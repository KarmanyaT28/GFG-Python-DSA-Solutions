'''Lowercase to Upercase
Difficulty: BasicAccuracy: 80.75%Submissions: 8K+Points: 1
You are given a string s. You need to convert the case of lowercase letter to uppercase letters.

Example 1:

Input:
Geeks
Output: 
GEEKS
Example 2:

Input:
for
Output: 
FOR
Your Task:

You only need to complete the function caseConversion() that takes s as parameter and returns the  converted string. 

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).

Constraints:
1 <= |s| <= 10000

'''


#User function Template for python3

class Solution:
    def caseConversion(self,s):
        return s.upper()