N = int(input())
count_2 = 0
count_3 = 0
for i in range(N):
    num = int(input())
    if num % 2 == 0:
        count_2 += 1
    if num % 3 == 0:
        count_3 += 1
print(f"2의 배수: {count_2}")
print(f"3의 배수: {count_3}")