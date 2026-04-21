while True:
    s, e = map(int, input().split())

    if not (1 < s < 10 and 1 < e < 10):
        print("INPUT ERROR!")
        continue

    if s > e:
        for A in range(1, 10):
            for B in range(s, e-1, -1):
                print(f"{B} * {A} = {A*B:2}", end="   ")
            print()
    else:
        for A in range(1, 10):
            for B in range(s, e+1):
                print(f"{B} * {A} = {A*B:2}", end="   ")
            print() 
    break
