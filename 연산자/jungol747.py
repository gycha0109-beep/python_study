lst = []
for i in range(3):
    nums = int(input())
    lst.append(nums)
print(True if lst[0] > lst[1] and lst[0] > lst[2] else False, True if lst[0] == lst[1] and lst[1] == lst[2] else False)
# ----------------------------------------------------------------
lst = [int(input()) for _ in range(3)]

# max() 함수와 set() 활용
is_max = lst[0] == max(lst) and lst.count(lst[0]) == 1 # 0번 인덱스가 유일한 최대값인지 확인
is_all_equal = len(set(lst)) == 1       # 모든 요소가 같은지 확인

print(is_max, is_all_equal)