T = int(input())
C = 0
for i in range(T):
    A, B = map(int, input().split())
    C += 1
    print(f"Case #{C}: {A} + {B} = {A+B}")
