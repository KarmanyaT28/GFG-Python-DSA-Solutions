'''Missing Characters in Panagram
Difficulty: BasicAccuracy: 41.51%Submissions: 18K+Points: 1Average Time: 15m
You are given a string s. You need to find the missing characters in the string to make a panagram ( a sentence using every letter of english alphabet at least once ).
Note: The output characters will be lowercase and lexicographically sorted.

 

Example 1:

Input:
s = Abcdefghijklmnopqrstuvwxy
Output: z
 

Example 2:

Input:
s = Abc
Output: defghijklmnopqrstuvwxyz
 

Your Task:

You only need to complete the function misssingPanagram() that takes s as parameter and returns -1 if the string is a panagram, else it returns a string that consists missing characters.

 

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).

 

Constraints:
1 <= |s| <= 10000

'''


class Solution:
    def missingPanagram(self, s):
        # 1. Convert to lowercase for uniform checking
        s = s.lower()
        
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        missing = ""
        
        # 2. Check each letter of the alphabet
        for char in alphabets:
            # 3. If the letter isn't in s, it's a missing character
            if char not in s:
                missing += char
        
        # 4. If string is empty, it's a panagram, return -1
        if missing == "":
            return -1
        
        # 5. Otherwise return the sorted missing characters
        return missing
    