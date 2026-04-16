N = int(input())
total = 0
for i in range(N):
    num = int(input())
    total += num
avg = total / N
print(f"sum: {total}")
print(f"avg: {avg:.1f}")