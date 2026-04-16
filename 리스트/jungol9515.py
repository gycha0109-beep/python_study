# 1. 6개의 입력 받기
nums = []
for i in range(6):
    nums.append(int(input("정수를 입력하시오. ")))

# 2. 연산들을 정의 (각 순서에 맞는 연산 함수들)
# 파이썬의 연산자들을 활용하여 리스트에 담습니다.
# (람다 함수를 사용하면 깔끔합니다)
ops = [
    lambda x: x + 3,
    lambda x: x - 3,
    lambda x: x * 3,
    lambda x: x // 3,
    lambda x: x % 3,
    lambda x: x ** 3
]

# 3. zip으로 입력값과 연산을 하나씩 짝지어 계산
results = []
for n, op in zip(nums, ops):
    results.append(op(n))

# 4. 결과 출력
print(*results)