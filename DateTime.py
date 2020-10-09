from dateutil.parser import parse
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

json ={'receivedDateTime': 'Wed Aug 19 13:27:15 2020'}

date= json['receivedDateTime']

j = parse(date)
k = datetime.now()
td = timedelta(days=2)
print(td)
print(k+td)
print(j+td)

# print(j.strftime('%d-%m-%Y %H:%M:%S'))
#
# format_string = '%d-%m-%Y %H:%M:%S'
#
datetime_object = datetime.strptime(j, format_string).date()
print("Hi i make changes in the branch")
# new_date = datetime_object + relativedelta(days=1)
#
# datetime_object= new_date.strftime('%d-%m-%Y %H:%M:%S')

#new_date = datetime_object + relativedelta(days=1)

#enddate= j.strftime('%d-%m-%Y %H:%M:%S') + datetime.timedelta(days=1)
# date_object = datetime.strptime(str(j), '%d-%m-%y')

# print(date_object)

print("date ",datetime_object)

