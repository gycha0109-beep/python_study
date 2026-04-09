K = int(input())
def gap(K):
    a, b, c = list(map(int, input().split()))
    for i in [a, b, c]:
        print(abs(K-i))
gap(K)

'''
K = int(input())
def gap(n):
    global K
    return abs(K-n)

a, b, c = (map(int, input().split()))

print(gap(a))
print(gap(b))
print(gap(c))
'''