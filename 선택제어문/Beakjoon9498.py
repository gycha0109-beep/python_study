N = int(input())

if 90 <= N <= 100:
    print("A")
elif 80 <= N <= 89:
    print("B")
elif 70 <= N <= 79:
    print("C")
elif 60 <= N <= 69:
    print("D")
else:
    print("F")

'''
N = int(input())
A = {10:"A", 9:"A", 8:"B", 7:"C", 6:"D"}
print(A.get(N // 10, "F"))
'''
