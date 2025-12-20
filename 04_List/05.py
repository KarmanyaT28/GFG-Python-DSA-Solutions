import math

class Solution:
    def median(self, arr):
        arr.sort()
        n = len(arr)
        
        if n%2==0:
            mid1 = n//2
            mid2 = mid1-1
            res = (arr[mid1]+arr[mid2])/2
            
        else:
            res = arr[n//2]
            
        return int(res)
            
    
    def mean(self, arr):
        mean = sum(arr)/len(arr)
        return int(mean)
            