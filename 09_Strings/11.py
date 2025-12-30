'''String Validation
Difficulty: EasyAccuracy: 49.22%Submissions: 10K+Points: 2
Given a string s representing a password, you need to check if the string is valid or not. A valid string has the following properties:

String must have the length greater than or equal to 10.
String must contain at least 1 numeric character.
String must contain at least 1 uppercase character.
String must contain at least 1 lowercase character.
String must contain at least 1 special character from @#$-*.
 

Example 1:

Input: eHello123@
Output: 1
Explanation: String is valid.

 

Example 2:

Input: hella
Output: 0
Explanation: String is not valid.
 

Your Task:
You don't need to read input or print anything. Complete the function validate() which takes string s as input parameter and returns true if the string is valid, else it returns false.

Constraints:
1 ≤ |s| ≤ 103

'''

#User function Template for python3

"""
input - 
s = string given 

output - 
return 0 if not validated else return true
"""

def validate(s):
    if len(s)<10:
        return 0
        
    has_num = False
    has_upper = False
    has_lower = False
    has_special = False
    
    special_chars = "@#$-*"
    
    for char in s:
        if char.isdigit():
            has_num = True
        elif char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char in special_chars:
            has_special = True
            
    if has_num and has_upper and has_lower and has_special:
        return 1
    else:
        return 0
            
            
            