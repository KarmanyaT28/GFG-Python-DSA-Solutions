'''Is Array Sorted
Difficulty: EasyAccuracy: 31.45%Submissions: 38K+Points: 2Average Time: 15m
Given an array a[ ] of size N. The task is to check if array is sorted or not. A sorted array can either be increasingly sorted or decreasingly sorted. Also consider duplicate elements to be sorted.

Example 1:

Input:
N = 5
a[] = {1, 1, 2, 2, 3}
Output: 
1
Explanation: 
Here, Given array a is increasingly sorted.
Example 2:

Input:
N = 2
a[] = {4, 2}
Output: 
1
Explanation:
Here, Given array a is decreasingly sorted.
Your Task:
You don't need to read input or print anything. You just need to complete the function isSorted() that takes arr and n as parameters and returns 0 if arr is unsorted and returns 1 if arr is sorted.

Constraints:
1 <= N <= 106
1 <= a[i] <= 106

'''

def isSorted(self, arr, n):
        # Check if original is same as increasingly sorted version
        inc = (arr == sorted(arr))
        
        # Check if original is same as decreasingly sorted version
        dec = (arr == sorted(arr, reverse=True))
        
        if inc or dec:
            return 1
        else:
            return 0
