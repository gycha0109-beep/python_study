from math import floor, ceil

def circle(N):
    X = N * N * 3.14
    A = floor(X)
    B = ceil(X)
    C = int(round(X))
    
    return f"원의 넓이\n버림 : {A}\n올림 : {B}\n반올림 : {C}"

radius = float(input())
result = circle(radius)
print(result)
