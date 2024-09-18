from datetime import datetime, timedelta
from argparse import ArgumentParser

def get_year_month():
    now = datetime.now()
    year = now.year

    parser = ArgumentParser()
    parser.add_argument('-m', type=int, help='month')
    arg = parser.parse_args()

    if arg.m is not None:
        args = arg.m
        if 1 <= args <= 12:
            month = args
        else:
            print(f'{args} is neither a month number (1..12) nor a name')
    else:
        month = now.month
    return (year, month)

def print_header(year, month):
    month_of_year = '{:^22}'.format(f'{month}月 {year}')
    print(month_of_year)

    weeeks = "月 火 水 木 金 土 日"
    print(weeeks)

def print_body(year, month):
    month_day_first = datetime(year, month, 1)
    if month == 12:
        month_day_last = datetime(year + 1, 1, 1) - timedelta(days=1)
    else:
        month_day_last = datetime(year, month + 1, 1) - timedelta(days=1)

    blanks = ["  " for num in range(month_day_first.weekday())]
    days = [f"{num:2d}" for num in range(1, month_day_last.day + 1)]
    days_of_month = blanks + days

    for day in range(0, len(days_of_month), 7):
        week = ''
        for week_days in range(day, day + 7):
            if len(days_of_month) <= week_days:
                break
            week += days_of_month[week_days] + ' '
        print(week)

def run():
    year, month = get_year_month()
    print_header(year, month)
    print_body(year, month)

if __name__ == "__main__":
    run()