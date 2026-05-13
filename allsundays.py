import datetime

def all_mondays(year):

    first_day = datetime.date(year, 1, 1)
    dw = first_day.weekday()
    days = datetime.timedelta(0 - dw)

    mon = first_day + days

    while mon.year == year:
        print(mon)
        mon += datetime.timedelta(7)

print(all_mondays(2026))