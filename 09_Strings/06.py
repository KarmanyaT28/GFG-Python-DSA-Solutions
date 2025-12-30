'''Reverse a String
Difficulty: BasicAccuracy: 69.49%Submissions: 443K+Points: 1Average Time: 15m
You are given a string s, and your task is to reverse the string.

Examples:

Input: s = "Geeks"
Output: "skeeG"
Input: s = "for"
Output: "rof"
Input: s = "a"
Output: "a"
Constraints:
1 <= s.size() <= 106
s contains only alphabetic characters (both uppercase and lowercase).

'''



#User function Template for python3

class Solution:
     def reverseString(self, s: str) -> str:
         s_list = list(s)
         s_list.reverse()
        #  print(s_list)
         
         new_arr = "".join(s_list)
         
         return new_arr