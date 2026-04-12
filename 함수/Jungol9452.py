def welcome():
    N, M = map(int, input().split())
    for i in range(N):
        print('Hello')
    print()
    for s in range(M):
        print('Hello')

welcome()

'''
# 재귀 정순
def number(N):
    if N > 0:
        print(N)
        number(N-1)
# 재귀 역순
def number(N):
    if N > 0:
        number(N-1)
        print(N)'''
# 함수가 전부 실행된 후 *쌓인 역순으로* 출력
