'''Panagram Checking
Difficulty: BasicAccuracy: 51.9%Submissions: 30K+Points: 1Average Time: 15m
You are given a string s. You need to find if the string is a panagram or not.

Note: A panagram contains all the letters of english alphabet at least once.

Examples:

Input: s = "Thequickbrownfoxjumpsoverthelazydog"
Output: True
Input: s = "HeavyDuty"
Output: False
Constraints:
1 <= |s| <= 104 

'''


class Solution:
    def isPanagram(self, s):
        # Convert to lowercase and filter to keep only alphabetic characters
        # Then count the unique characters
        letters_found = set()
        for char in s.lower():
            if 'a' <= char <= 'z':
                letters_found.add(char)
        
        return len(letters_found) == 26