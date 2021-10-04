import datetime as dt  #using datetime module as dt
now = dt.datetime.now()
#from dt module and from datetime class we r using now method to get current date and time
day = now.today().weekday()
year = now.year
date_of_birth = dt.datetime(year=1997,month=10,day=16)
print(now)
print(day)
print(year)
print(date_of_birth)