'''
A = ['a', 'b', 'c', 'd', 'e']
print(A)
for i in A[::-1]:
    print(i, end = ' ')
'''

A = ['a', 'b', 'c', 'd', 'e']
print(A)
length = len(A)
i = 1
while i <= length:
    print(A[length-i], end = ' ')
    i += 1