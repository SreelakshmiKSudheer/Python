import random
import datetime

birthday = []
i = 0

while(i < 50):
    year = random.randint(1895,2022)
# the oldest person ever lived was 122 years old

    if(year % 400 == 0 or year % 4 == 0 and year % 100 != 0): 
        leap = 1
    else:
        leap = 0
        
        
    month = random.randint(1, 12)
    
    
    if(month == 2 and leap == 1):
        date = random.randint(1, 29)
        
    elif(month == 2 and leap != 1):
        date = random.randint(1,28)
        
    elif((month % 2 == 0 and month < 7) or (month % 2 != 0 and month > 7)):
        date = random.randint(1,30)
        
    elif((month % 2 == 0 and month > 7) or (month % 2 != 0 and month <= 7) ):
        date = random.randint(1,31)
        
    dd = datetime.date(year,month,date)
    day_of_year = dd.timetuple().tm_yday
    
    i += 1
    birthday.append(day_of_year)
    
birthday.sort()

i = 0

while(i < 50):
    print(birthday[i])
    i += 1
    
