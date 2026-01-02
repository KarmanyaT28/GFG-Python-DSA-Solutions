# Sorted in Python

l = [10, 20, 14]
ls = sorted(l)

print(l)
print(ls)

# sorted(iterable, key, reverse)



l = [10, -15, -2, 1]
ls = sorted(l, key=abs, reverse=True)
print(ls)


'''Time Complexity: O(n log(n))
Space Complexity: O(n)'''




t = (10,12,5,1)
print(sorted(t))

s = {'gfg','courses','python'}
print(sorted(s))

st = 'gfg'
print(sorted(st))

d = {10:'gfg',15:'ide',5:'courses'}
# print("The d sort")
print(sorted(d))

l = [(10,15),(1,8),(2,3)]
print(sorted(l))



'''Time Complexity: O(n log(n))
Space Complexity: O(n)'''