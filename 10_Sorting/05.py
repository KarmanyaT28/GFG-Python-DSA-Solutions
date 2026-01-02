# Stability in Sorting Algorithm

# A sorting algorithm is said to be stable if two objects with equal keys appear in the same order in sorted output as they appear in the input data set.


l=[("Anil",50),("Piyush",50),("Ram",80)]
l.sort()
print(l)


# Time Complexity: O(n log(n))
# Space Complexity: O(1)


'''Which sorting algorithms are stable? 

Some Sorting Algorithms are stable by nature, such as Bubble Sort, Insertion Sort, Merge Sort, Count Sort, etc.

BIMC
 

Which sorting algorithms are unstable? 

Quick Sort, Heap Sort etc., can be made stable by also taking the position of the elements into consideration

QH

'''