def number(N):
    if N > 0:
        return 'PLUS'
    elif N < 0:
        return 'MINUS'
    else:
        return 'ZERO'

A = int(input())
NUMBER = number(A)
print(NUMBER)