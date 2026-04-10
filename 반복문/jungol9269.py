N = int(input())
lst = []
while N > 0:
    lst.append(N)
    N -= 3
print(*lst)