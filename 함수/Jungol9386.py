'''N = int(input())
pi = 3.14
print(f"PI = {pi}")
print(f"Area = {N} * {N} * {pi} =", round(N**2*pi, 1))
'''

def Pi():
    return 3.14

def circle(N, pi):
    return round(N**2*pi, 1)

def OP(N, pi):
    return f"Area = {N} * {N} * {pi} ="

A = int(input())
pi = Pi()
area = circle(A, pi)

print(f"PI = {pi:.1f}")
print(OP(A, pi), area)