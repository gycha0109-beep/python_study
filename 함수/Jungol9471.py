def qwer(a, b, c):
    return f"max: {max(a, b, c)}\nmin: {min(a, b, c)}"

A, B, C = map(int, input().split())
result = qwer(A, B, C)
print(result)
