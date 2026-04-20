TC = int(input())

for OX in range(1, TC+1):   
    banbock = input()
    total = 0
    Plus_O = 0
    
    for i in banbock:
        if str(i) == 'O':
            Plus_O += 1
            total += Plus_O
        else:
            Plus_O = 0 

    print(total)     
