import calendar
year = int(input("Enter year as a numbers: "))
month = int(input("Enter month as a numbers: "))
cal = calendar.month(year, month)
print(cal)
