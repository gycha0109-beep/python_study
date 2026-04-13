A = []
for i in range(5):
    N = int(input())
    A.append(N)        # A = [int(input()) for _ in range(5)]

B = A[::-1]
C = B.copy()

bonus = int(input())
C.append(bonus)         # C.append(int(input()))

print('A =',A)
print('B =',B)
print('C =',C)
