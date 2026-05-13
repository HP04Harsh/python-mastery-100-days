import datetime

def monday(year):
    first_day = datetime.date(year, 1, 1)
    dw = first_day.weekday()

    days_until_monday = (7 - dw) % 7
    mon = first_day + datetime.timedelta(days_until_monday)

    while mon.year == year:
        print(mon)
        mon += datetime.timedelta(7)

monday(2026)