TC = int(input())

total = 0
Plus_O = 0
for OX in range(1, TC+1):   
    banbock = str(input())
    
for i in OX[0:len(OX)]:
    if str(i) == 'O':
        Plus_O += 1
        total += Plus_O
    else:
        Plus_O = 0 
print(OX)
# OX의 [0]부터 len(OX+1)까지 인덱스