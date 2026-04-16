""" a = int(input())
print(a+a*11+a*111+a*1111) """
#--------------------------------------------------
a = input()
total = 0

for i in range(1, 5):
    num = int(a * i) 
    total += num

print(total)