def plus(N):
    i = 1
    total = 0
    while i <= N:
        total += i
        i += 1
    return total


num = int(input())
A = plus(num)
print(A)