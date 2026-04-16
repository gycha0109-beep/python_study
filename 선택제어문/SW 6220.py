""" def U_L(word):
    if word.isupper():
        return '대문자'
    else:
        return '소문자'

TC = int(input())

for i in range(1, TC + 1):
    alpha = input()
    S = U_L(alpha)
    print(f'#{i} {alpha} 는 {S} 입니다.') """

def ask(word):
    code = ord(str(word))
    if 65 <= code <= 90:
        return '대문자'
    elif 97 <= code <= 122:
        return '소문자'

TC = int(input())

for i in range(1, TC + 1):
    alpha = input()
    S = ask(alpha)
    print(f'#{i} {alpha} 는 {S} 입니다.')