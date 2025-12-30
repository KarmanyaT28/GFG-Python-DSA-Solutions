'''Count Words in String
Difficulty: BasicAccuracy: 66.28%Submissions: 29K+Points: 1
You are given a string s consisting of multiple words. You need to count the total words in the string. Words are separated by a single space.
Note: It is guaranteed that the last character of the given string is not a white space.

Examples:

Input: s = "Geeks"
Output: 1
Explanation: There is just one word in the given sentence
Input: s = "World is hello"
Output: 3
Explanation: There exists three words in the given sentence
Constraints:
1 <= |s| <= 104

'''


#User function Template for python3

class Solution:
    def countWords(self,s):
        
        count = 1
        
        for char in s:
            if char==" ":
                count=count+1
            
        return count