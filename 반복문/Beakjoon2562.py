num = []
for i in range(9):
    A = int(input())
    num.append(A)
print(max(num))
print(num.index(max(num))+1)