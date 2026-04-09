N = int(input())

end = 1      # 현재 층의 끝 숫자
step = 6     # 증가량
layer = 1    # 층

while N > end:
    end += step
    step += 6
    layer += 1

print(layer)