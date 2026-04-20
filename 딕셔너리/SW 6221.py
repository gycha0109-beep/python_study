RSP = ["가위","바위","보"]
Man1, Man2 = input(), input()
win_case = {
    RSP[0]: RSP[2],  # 가위 - 보
    RSP[1]: RSP[0],  # 바위 - 가위
    RSP[2]: RSP[1]   # 보 - 바위
}
if Man1 == Man2:
    print("Result : Draw")
elif win_case[Man1] == Man2:
    print("Result : Man1 Win!")
else:
    print("Result : Man2 Win!")