""" def qwer(a, b, c, d, e, f, g, h, i, j):
    if -100 <= a <= 100 and -100 <= b <= 100 and -100 <= c <= 100 and-100 <= d <= 100 and-100 <= e <= 100 and-100 <= f <= 100 and-100 <= g <= 100 and-100 <= h <= 100 and-100 <= i <= 100 and-100 <= j <= 100:
        return abs(a)+abs(b)+abs(c)+abs(d)+abs(e)+abs(f)+abs(g)+abs(h)+abs(i)+abs(j)
A,B,C,D,E,F,G,H,I,J = map(int,input().split())
result = qwer(A,B,C,D,E,F,G,H,I,J)
print(result) """

def qwer(nums):
    total = 0
    for i in nums:
        if not -100 <= i <= 100:
            continue
        total += abs(i)
    return total

result = list(map(int, input().split()))
print(qwer(result))
