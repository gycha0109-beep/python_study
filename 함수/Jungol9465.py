def plus(N):
    for i in range(1, N+1, 1):
        i += i
    return i

num = int(input())
A = plus(num)
print(A)