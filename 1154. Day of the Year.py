"""
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
"""

from datetime import datetime

date = '2019-01-09'
subtract_date = date[:4]+'-01-01'

date = datetime.strptime(date, '%Y-%m-%d')
subtract_date = datetime.strptime(subtract_date, '%Y-%m-%d')

print((date - subtract_date.days) + 1)