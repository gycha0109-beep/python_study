gender, age = input().split()
age = int(age)
if gender  == 'M' and age >= 19:
    print('MAN')
elif gender == 'F' and age >= 19:
    print('WOMAN')
elif gender == 'M' and age < 19:
    print('BOY')
elif gender == 'F' and age < 19:
    print('GIRL')