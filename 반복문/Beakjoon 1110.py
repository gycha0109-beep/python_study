N = input()
start = int(N)
num = int(N)
count = 0
while True:
    a = num % 10
    b = num // 10
    num = a*10 + (a+b)%10
    count += 1
    if num == start:
        break
print(count)