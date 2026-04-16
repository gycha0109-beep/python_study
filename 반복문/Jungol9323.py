def mul(N, M):
    for i in range(1, 10):
        if N <= M:
            for j in range(N, M+1):
                print(f"{j} * {i} = {j * i}", end = "   ")
        elif N >= M:
            for j in range(N, M-1, -1):
                print(f"{j} * {i} = {j * i}", end = "   ")
        print()

S = int(input())
E = int(input())
mul(S, E)
