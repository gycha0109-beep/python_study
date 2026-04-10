S = int(input())
E = int(input())
lst = []
while S >= E:
    lst.append(S)
    S -= 1
print(*lst)