# OLUPOT ROBERT
# REG NO. 16/U/18969
#COMPUTER ENGINEERING
#importing calendar module so that i can use the calendar
import calendar
#importing datetime module from python library
from datetime import datetime
#extracting the current system time and date
now=datetime.now()
#extracting current date only without time
current_date=now.date()
yea=list(str(current_date))#lists the current date
current_day=int(yea[-2]+yea[-1])#extracts the current day of the month and converts it to an integer
current_month=int(yea[5]+yea[6])#extracts the current month  and converts it to an integer
year=int(yea[0]+yea[1]+yea[2]+yea[3])#extracts the current  and converts it to an integer
age=int(input('Enter your age: '))
mt=int(input('Enter the month you were born: '))
dy=int(input('Enter the day of the month you were born: '))
if mt>current_month:
        yr=year-age-1
elif mt==current_month:
    if dy>current_day:
        yr=year-age-1
    else:
        yr=year-age
else:
    yr=year-age
cal=(calendar.weekday(yr, mt, dy))
day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saterday','Sunday']
print ('You where born on' , day[cal])


