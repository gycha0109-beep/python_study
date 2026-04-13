A = []
for i in range(5):
    N = int(input())
    A.append(N)
B = A.copy()
C = A[::-1]
for i2 in range(3):
    N = int(input())
    B.append(N)
print(C)
print(B)
print(A)