def qwer(a, b, c, d):
    x = a if abs(a) > abs(b) else b
    y = c if abs(c) < abs(d) else d
    return x, y
A, B = map(int, input().split())
C, D = map(float, input().split())
res1, res2 = qwer(A,B,C,D)
print(res1)
print(res2)
