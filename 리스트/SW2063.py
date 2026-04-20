def solution(array):
    array.sort()
    return array[len(array)//2]

N = int(input())
Nums = list(map(int, input().split()))
result = solution(Nums)
print(result)