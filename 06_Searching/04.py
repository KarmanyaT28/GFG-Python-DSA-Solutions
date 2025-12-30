'''Count 1's in binary array
Difficulty: EasyAccuracy: 49.3%Submissions: 66K+Points: 2Average Time: 20m
You are given a binary array that is sorted in non-increasing order, meaning all the 1's appear before the 0's. Find the total number of 1's present in the array.

Examples:

Input: arr[] = [1, 1, 1, 1, 1, 0, 0, 0]
Output: 5
Explaination: Count of 1's in the array is 5.
Input: arr[] = [1, 1, 1, 1, 1, 1, 1]
Output: 7
Explaination: Count of 1's in the array is 7.
Constraints:
1 ≤ arr.size() ≤ 105 
0 ≤ arr[i] ≤ 1

'''


class Solution:
    def countOnes(self, arr):
        n = len(arr)
        count=0
        for i in range(0,n):
            if arr[i]==1:
                count = count+1
            i=i+1
            
        return count