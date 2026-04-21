def switch(a, b):
    a, b = b, a
    return f"함수 내부: a = {a}, b = {b}"

a, b = map(int,input().split())

change = switch(a, b)

print(change)
print(f"함수 외부: a = {a}, b = {b}")
a, b = b, a
print(change)
print(f"함수 외부: a = {a}, b = {b}")