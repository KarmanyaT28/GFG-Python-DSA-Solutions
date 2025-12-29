'''Print Array Elements Using Recursion
Difficulty: BasicAccuracy: 56.49%Submissions: 16K+Points: 1
You are given an array arr of size n. You need to print the array elements from start to end using given recursive function.


Example 1:

Input:
n = 5
arr[] = {1,2,3,4,5}
Output: 1 2 3 4 5

Example 2:

Input:
n = 4
arr[] = {5,4,2,1}
Output: 5 4 2 1
 

Your Task:
Complete the function printArrayRecursively() that takes array and size n as parameters and prints the array elements recursively. The newline is provided by driver code.


Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N) (Recursive).

'''


class Solution:
    def printArrayRecursively(self,arr,n):
        #code here
        if n==0:
            return
        print(arr[-n],end=' ')
        self.printArrayRecursively(arr,n-1)
