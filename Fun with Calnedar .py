from datetime import datetime as dt
import calendar as cl

'''
print(dt.now())
print(cl.weekday(2023,10,27))       # weekday(int year,int month,int day)
'''

 # time.time -- time in ms since Jan 1, 1970
 # ord()  -- convert a character into its ASCII notation

weekdays = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
 
def is_leap_year(year):
    
    if (year % 400 == 0):
        return True
    elif (year % 100 == 0):
        return False
    elif (year % 4 == 0):
        return True
    else:
        return False

def max_days(month,year):
     
    if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        return 31
    elif(month == 4 or month == 6 or month == 9 or month == 11):
        return 30
    elif month == 2:
        if(is_leap_year(year) == True):
            return 29
        else:
            return 28
    else:
        return -1
        
# year
while True:
    year = int(input("Enter year(1970 - present) : "))
    if year < 1970:
        print("Enter a year in the range 1970 till present ")
    else:
        break
    
# month    
while True:
    month = int(input("Enter month :"))
    if month > 0 and month < 12:
        break
    else:
        print("Enter a valid month no.(1 - 12) : ")

# date    
while True:
    date = int(input("Enter day :"))
    
    if(date <= max_days(month,year)):
        break
    else:
        print("Enter a valid date")


def date_to_day(day_index):
    
    if(day_index > 0 and day_index <= 7):
        return weekdays[day_index + 1]
    
day_index = cl.weekday(year, month, date)
print("Weekaday is ",date_to_day(day_index))

