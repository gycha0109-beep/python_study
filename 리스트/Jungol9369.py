lst = []
for i in range(100):
    N = int(input())
    if N == -1:
        break
    lst.append(N)
print(*lst[-3:])