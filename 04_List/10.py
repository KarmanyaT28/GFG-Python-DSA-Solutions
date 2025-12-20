'''Who has the majority?
Difficulty: BasicAccuracy: 44.36%Submissions: 118K+Points: 1
Given an array arr[] and two elements x and y, return the element that occurs more frequently. If both elements have the same frequency, return the smaller one.

Examples:

Input: arr[] = [1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5], x = 4, y = 5
Output: 4
Explanation: frequency of 4 is 4.frequency of 5 is 1.Since 4>1 so return 4
Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8], x = 1, y = 7
Output: 1
Explanation: frequency of 1 is 1.frequency of 7 is 1.Since 1 < 7, return 1.
Constraints:
1 ≤ arr.size() ≤ 106
0 ≤ arr[i] , x , y ≤ 108

'''


class Solution:
    def moreFrequent(self, arr, x, y):
        countX = 0
        countY = 0
        
        n = len(arr)
        
        for i in range(0,n):
            if arr[i]==x:
                countX+=1
                
            if arr[i]==y:
                countY+=1
                
        
        if countX>countY:
            return x
        elif countY>countX:
            return y
        else:
            return min(x,y)
        