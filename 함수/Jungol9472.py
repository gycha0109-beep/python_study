def qwer(a, b, c, d, e):
    return max(a, b, c, d, e) - min(a, b, c, d, e)
    
A, B, C, D, E = map(int, input().split())
result = qwer(A, B, C, D, E)
print(result)
