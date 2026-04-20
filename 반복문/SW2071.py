TC = int(input())
for i in range(1, TC+1):
    nums = list(map(int, input().split()))
    total = 0
    for j in nums:
        total += j
    print(f"#{i} {round(total/len(nums))}")