import datetime

count = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        try:
            date = datetime.date(year, month, 1)

            if date.isoweekday() == 7:
                count = count + 1
        except ValueError:
            pass

print(count)
