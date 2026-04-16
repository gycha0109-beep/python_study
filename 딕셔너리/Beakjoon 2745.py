N, B = input().split()
B = int(B)

num_dict = {str(i): i for i in range(10)}
num_dict.update({chr(i + 55): i for i in range(10, 36)})

total = 0
square = len(N) - 1

index = 0
while index < len(N):
    total += num_dict[N[index]] * (B ** square)
    index += 1
    square -= 1

print(total)

""" n, b = input().split()  # int의 두번째 파라미터 값으로                      
print(int(n, int(b)))         들어가는 숫자는 진법을 의미한다
 """