N = int(input())
def number(N):
    if N < 0:
        return "negative"
    elif N > 0:
        return "positive"
    else:
        return "zero"
print(number(N))