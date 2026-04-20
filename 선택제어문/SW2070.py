TC = int(input())
for i in range(1, TC+1):
    A, B = map(int, input().split())
    if A > B:
        print(f"#{i} >")
    elif A < B:
        print(f"#{i} <")
    else:
        print(f"#{i} =")