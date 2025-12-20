'''Find Immediate Smaller Than X
Difficulty: EasyAccuracy: 39.03%Submissions: 56K+Points: 2Average Time: 15m
Given an array arr[] of size N containing positive integers and an integer X, find the element in the array which is smaller than X and closest to it.

 

Example 1:

Input:
N = 5
arr[] = {4 67 13 12 15}
X = 16
Output: 15
Explanation: For a given value 16, there
are four values which are smaller than
it. But 15 is the number which is smaller
and closest to it with minimum difference
of 1.
 

Example 2:

Input:
N = 5
arr[] = {1 2 3 4 5}
X = 1
Output: -1
Explanation: No value is smaller than 1.
 

Your Task:
You don't need to read input or print anything. You need to complete the given function immediateSmaller() which takes arr, N and X as input parameters and returns the closest element that is smaller than X. If no such element exists, return -1.

 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

 

Constraints:
1 <= N <= 103
1 <= arr[i], X <= 104

Topic'''


class Solution:
    def immediateSmaller(self,arr,n,x):
        arr1 = []
        for i in range(0,n):
            if arr[i]<x:
                arr1.append(arr[i])
        if len(arr1)==0:
            return -1
        return max(arr1)