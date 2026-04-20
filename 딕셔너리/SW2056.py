T = int(input())

months = range(1, 13)
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
last_day = dict(zip(months, days))

for tc in range(1, T + 1):
    date = input()

    year = date[:4]
    month = int(date[4:6])
    day = int(date[6:])

    if month in last_day and 1 <= day <= last_day[month]:
        print(f"#{tc} {year}/{month:02d}/{day:02d}")
    else:
        print(f"#{tc} -1")