# Days in month

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(input_year, input_month):
    if input_month > 12 or input_month < 1:
        return "Invalid month"
    input_month = input_month - 1
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year=input_year):
        month_days[1] = month_days[1] + 1 # Adjust February for leap year
    month_day = month_days[input_month]
    return month_day


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
