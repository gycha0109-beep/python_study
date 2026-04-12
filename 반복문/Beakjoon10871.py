N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in A:
    if i < X:
        print(i, end=" ")

'''
N, X = map(int, input().split())
A = (*[i for i in map(int, input().split()) if i < X])
print(*A)
'''
