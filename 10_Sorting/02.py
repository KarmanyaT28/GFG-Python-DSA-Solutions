# List Sort in Python


# sort() method sorts the list in ascending order by default, it can also sort the list in descending order by using reverse=True inside sort() and it can also sort the list in custom order.

l1 = [5,10,23,11,45,76,22,11,1]
l1.sort()
print(l1)


l2 = [45,34,21,66,99,77]
l2.sort(reverse = True)
print(l2)


l3 = ['gfg','ide','courses']
l3.sort()
print(l3)


def myFun(s):
    return len(s)

ll = ['gfg', 'courses', 'python']
ll.sort(key=myFun)
print(ll)

ll.sort(key=myFun, reverse=True)
print(ll)


# Time Complexity: O(n log(n))
# Space Complexity: O(1)


print("##############################################################")

# The below example sorts the list in increasing order based on the first value of pair


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


def myFun(p):
    return p.y


lis = [Point(1,15),Point(10,5),Point(3,8)]

lis.sort(key=myFun)


for i in lis:
    print(i.x,i.y)

'''
Time Complexity: O(n log(n))
Space Complexity: O(1)


'''






