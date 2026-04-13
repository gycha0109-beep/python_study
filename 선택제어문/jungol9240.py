from ast import Continue

def gap(N, M):
    if not 0 <= N <= 100 and 0 <= M <= 100:
        Continue
    return N-M if N > M else M-N
A, B = map(int,(input().split()))   
qwer = gap(A, B)
print(qwer)