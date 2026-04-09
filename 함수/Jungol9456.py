a, b, c = map(int, input().split())
def func(x):
    return a*x**2 + b*x + c
for i in [2,3,5]:
    print(func(i))