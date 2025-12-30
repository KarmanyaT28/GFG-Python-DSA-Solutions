'''Uppercase to Lowercase
Difficulty: EasyAccuracy: 88.98%Submissions: 7K+Points: 2
You are given a string s. You need to convert the case of uppercase letters to lowercase letters.

Example 1:

Input:
GeekS

Output: 
geeks
Example 2:

Input:
FOR

Output: 
for
Your Task:

You only need to complete the function caseConversion() that takes s as parameter and returns the converted string. 

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).

Constraints:
1 <= |s| <= 10000

'''


#User function Template for python3

"""
input -
@s :- string to be converted

output - 
return converted string 
"""
class Solution:
    def caseConversion(self,s):
       return s.lower()
