'''Vowels in String
Difficulty: BasicAccuracy: 81.41%Submissions: 6K+Points: 1
You are given a string s. You need to count the total vowels in the string. The string s contains lowercase letters only.

Example 1:

Input:
s = geeks
Output: 
2
Example 2:

Input:
s = world
Output: 
1
Your Task:

You only need to complet the function countVowels() that takes s as parameter and returns the count of vowels in the string. 

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).

Constraints:
1 <= |s| <= 10000

'''


#User function Template for python3

class Solution:
    def countVowels(self,s):
        count=0
        
        vowels=['a','e','i','o','u']
        
        for char in s:
            if char in vowels:
                count=count+1
                
                
        return count