N = int(input())
num = 1
count = 0
while num <= N:
    if num % 3 == 0:
        count += 1
    num += 1
print(count)