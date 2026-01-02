# Bubble Sort Algorithm
# Bubble Sort is the simplest sorting algorithm that works by repeatedly 
# swapping the adjacent elements if they are in the wrong order. 
# This algorithm is not suitable for large data sets as its 
# average and worst-case time complexity is quite high.


# How does Bubble Sort Work?

# Input: arr[] = {5, 1, 4, 2, 8}

# First Pass: 

# Bubble sort starts with very first two elements, comparing them to check which one is greater.
# ( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1. 
# ( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4 
# ( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2 
# ( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.


# Second Pass: 

# Now, during second iteration it should look like this:
# ( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ) 
# ( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2 
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) 
# ( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 ) 



# Third Pass: 

# Now, the array is already sorted, but our algorithm does not know if it is completed.
# The algorithm needs one whole pass without any swap to know it is sorted.
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) 
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) 
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) 
# ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) 



# Bubble Sort Code


def bubblesort(l):
    n = len(l)


    for i in range(n-1):

        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]

    
l = [10,8,20,5]

bubblesort(l)

print(l)

print(*l)


# The below code slightly optimized the bubble sort ( basically it stops when list become sorted ).


def bubbleSort(l):
    n = len(l)

    for i in range(n-1):
        swapped = False

        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]

                swapped = True

        if swapped == False:
            return
        

l = [10, 8, 20, 5]


bubbleSort(l)

print(*l)



# Time Complexity: O(n2)
# Space Complexity: O(1)


