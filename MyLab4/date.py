#1 

from datetime import datetime,timedelta 
current_time=datetime.today()
substructed_time=current_time-timedelta(5)
print("Today's date :", current_time.strftime("%Y-%m-%d"))
print("Date 5 days before:", substructed_time.strftime("%Y-%m-%d"))

#2 

from datetime import datetime,timedelta
current_time=datetime.today()
yesterday=current_time-timedelta(1)
tomorrow=current_time+timedelta(1)
print("Yesterday's date was:",yesterday.strftime("%Y-%m-%d"))
print("Today's date is:",current_time.strftime("%Y-%m-%d"))
print("Tommorows's date will be:",tomorrow.strftime("%Y-%m-%d"))

#3 

from datetime import datetime
time=datetime.now()
without_millisec=time.strftime("%Y-%m-%d,%H:%M:%S")  #code automatically doesn't take milliseconds
print(without_millisec)

""" 
or just like this 

from datetime import datetime

current_datetime = datetime.now()

new_datetime = current_datetime.replace(microsecond=0)

print("Original datetime:", current_datetime)
print("Datetime without microseconds:", new_datetime)

"""

#4 

from datetime import datetime,timedelta

yesterday = datetime.now() - timedelta(1)
tomorrow = datetime.now() + timedelta(1)

difference=tomorrow-yesterday  
print(difference.total_seconds()) 
