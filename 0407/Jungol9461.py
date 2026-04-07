def cal(n1, n2):
    n1, n2 = map(int, input().split())
    return max(n1, n2) // 2, min(n1, n2) * 2
print(cal())