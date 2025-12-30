'''Peak element
Difficulty: MediumAccuracy: 38.86%Submissions: 611K+Points: 4Average Time: 30m
You are given an array arr[] where no two adjacent elements are same, find the index of a peak element. An element is considered to be a peak if it is greater than its adjacent elements (if they exist).

If there are multiple peak elements, Return index of any one of them. The output will be "true" if the index returned by your function is correct; otherwise, it will be "false".

Note: Consider the element before the first element and the element after the last element to be negative infinity.

Examples :

Input: arr = [1, 2, 4, 5, 7, 8, 3]
Output: true
Explanation: arr[5] = 8 is a peak element because arr[4] < arr[5] > arr[6].
Input: arr = [10, 20, 15, 2, 23, 90, 80]
Output: true
Explanation: Element 20 at index 1 is a peak since 10 < 20 > 15. Index 5 (value 90) is also a peak, but returning any one peak index is valid.
Constraints:
1 ≤ arr.size() ≤ 106
-231 ≤ arr[i] ≤ 231 - 1

'''

# class Solution:
#     def peakElement(self, arr):
#         n = len(arr)
        
#         def find_peak(low, high):
#             # Calculate mid index
#             mid = low + (high - low) // 2
            
#             # 1. Compare mid with its neighbors
#             # Check if mid is greater than left neighbor (if it exists)
#             # AND greater than right neighbor (if it exists)
#             left_ok = (mid == 0 or arr[mid] > arr[mid - 1])
#             right_ok = (mid == n - 1 or arr[mid] > arr[mid + 1])
            
#             if left_ok and right_ok:
#                 return mid
            
#             # 2. If the right neighbor is greater, a peak is in the right half
#             if mid < n - 1 and arr[mid + 1] > arr[mid]:
#                 return find_peak(mid + 1, high)
            
#             # 3. Otherwise, a peak is in the left half
#             else:
#                 return find_peak(low, mid - 1)
        
#         return find_peak(0, n - 1)



class Solution:
    def peakElement(self, arr):
        n = len(arr)

        for i in range(n):

            if i == 0:
                left = float('-inf')
            else:
                left = arr[i - 1]

            if i == n - 1:
                right = float('-inf')
            else:
                right = arr[i + 1]

            if arr[i] > left and arr[i] > right:
                return i



class Solution:
    def peakElement(self, arr):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if (mid == 0 or arr[mid] > arr[mid - 1]) and \
               (mid == len(arr) - 1 or arr[mid] > arr[mid + 1]):
                return mid

            elif mid < len(arr) - 1 and arr[mid] < arr[mid + 1]:
                low = mid + 1   # go right
            else:
                high = mid - 1  # go left
