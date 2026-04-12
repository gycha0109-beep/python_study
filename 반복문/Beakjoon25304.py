X = int(input())
N = int(input())

total = 0 # c = []
for t in range(N):
    a,b = map(int, input().split())
    total += a*b # c.append(a*b)

if X == total: # if X == sum(c)
    print("Yes")
else:
    print("No")
