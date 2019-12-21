import datetime
import calendar


def findDay(date): #defining function for finding a  day
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])


date = '26 09 1996'
print(findDay(date)) #printing plus calling findDay function here