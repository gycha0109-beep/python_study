one = int(input())
two = int(input())
if one >= 3 and two >= 3:
    print('High')
elif one < 3 and two < 3:
    print('Low')
elif one >= 3 or two >= 3:
    print('Mid')