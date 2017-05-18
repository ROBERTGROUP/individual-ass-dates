# OLUPOT ROBERT
# REG NO. 16/U/18969
#COMPUTER ENGINEERING
import calendar
from datetime import datetime
now=datetime.now()
ye=now.date()
yea=list(str(ye))
pat=int(yea[-2]+yea[-1])
nat=int(yea[5]+yea[6])
year=int(yea[0]+yea[1]+yea[2]+yea[3])
age=int(input('Enter your age: '))
mt=int(input('Enter the month you were born: '))
dy=int(input('Enter the day of the month you were born: '))
if mt>nat:
        yr=year-age-1
elif mt==nat:
    if dy>pat:
        yr=year-age-1
    else:
        yr=year-age
else:
    yr=year-age
cal=(calendar.weekday(yr, mt, dy))
day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saterday','Sunday']
print ('You where born on' , day[cal])


