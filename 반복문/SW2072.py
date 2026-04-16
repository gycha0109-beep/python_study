T = int(input())
for i in range(T):
    numbers = list(map(int, input().split()))
    total = 0
    for j in numbers:
        if j % 2 == 1:
            total += j
    print(f"#{i+1} {total}")