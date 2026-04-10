def ABC():
    gender, age = input().split()
    age = int(age) # 괄호 안에 변수를 넣어서 정수로 변환
    
    if gender in ['M', 'm']: # 성별이 M 또는 m일 때
        if age >= 20:
            return "MAN"
        else:
            return "BOY"
    elif gender in ['F', 'f']: # 성별이 F 또는 f일 때
        if age >= 20:
            return "WOMAN"
        else:
            return "GIRL"

print(ABC())