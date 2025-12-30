'''Count Distinct Vowels in String
Difficulty: BasicAccuracy: 67.52%Submissions: 9K+Points: 1
You are given a string s. You need to count the total distinct vowels in the string. The string s contains lowercase letters only.

Example 1:

Input:
geeks

Output: 
1
Example 2:

Input:
world

Output:
1
Your Task:

You only need to complete the function countVowels() that takes s as parameter and returns the count of distinct vowels in the string. 

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).

Constraints:
1 <= |s| <= 10000

'''


#User function Template for python3

class Solution:
    def countVowels(self,s):
        vowels = ['a','e','i','o','u']
        
        
        count=0
        
        
        for char in s:
            if char in vowels:
                count=count+1
                
                vowels.remove(char)
           
        return count