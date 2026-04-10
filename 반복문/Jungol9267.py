N = int(input())
lst = []
while N > 4:
    lst.append(N)
    N -= 1
print(*lst)