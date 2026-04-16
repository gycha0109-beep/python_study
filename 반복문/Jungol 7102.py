even_count = 0
odd_sum = 0
N = int(input())
for i in range(N):
    num = int(input())
    if num % 2 == 0:
        even_count += 1
    else:
        odd_sum += num
print(odd_sum, even_count)
