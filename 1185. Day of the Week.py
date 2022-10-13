"""
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
"""
from datetime import datetime
day = 18
month = 7
year = 1999

weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# print(datetime.isoweekday(datetime(year, month, day)))
print(weekday[datetime.isoweekday(datetime(year, month, day)) - 1])