def cal(N, M):
    A = N%2
    B = M+10
    return A, B, A+B

N, M = map(int, input().split())
a, b, c = cal(N, M)
print(*cal(N, M))
