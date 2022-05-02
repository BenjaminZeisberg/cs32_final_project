import datetime
import re

list_dates = ['2022-04-23 07:02:38 PM', '2022-04-23 07:04:37 PM', '2022-04-23 07:07:02 PM', '2022-04-23 07:07:33 PM', '2022-04-23 07:09:59 PM', '2022-04-23 07:16:06 PM']


# new_date = re.split('-', ' ', ':', date1)
# print(new_date)
date1 = re.split('\ |:|-', list_dates[1])
date1.pop()

date2 = re.split('\ |:|-', list_dates[2])
date2.pop()

for items in date1:
    dic = {'year': date1[0], 'month': date1[1], 'day': date1[2], 'hour': date1[3], 'minute': date1[4], 'seconds': date1[5]}
    dic2 = {'year': date2[0], 'month': date2[1], 'day': date2[2], 'hour': date2[3], 'minute': date2[4], 'seconds': date2[5]}


dt1 = datetime.datetime(int(dic['year']), int(dic['month']), int(dic['day']), int(dic['hour']), int(dic['minute']), int(dic['seconds']))
dt2 = datetime.datetime(int(dic2['year']), int(dic2['month']), int(dic2['day']), int(dic2['hour']), int(dic2['minute']), int(dic2['seconds']))

#difference = dt2 - dt1
# print(difference)

# time = '07:02:38'
# time

list1 = [['42.37947', '-71.12459'], ['42.37632', '-71.12346'], ['42.37284', '-71.12177']]
list2 = [9.0, 145.0, 31.0]

final_list = []
for i in range(0,len(list1)):
    new_list = [(list1[i], list2[i])]
    final_list.append(new_list)

test_list = [[list1, list2] for list1, list2 in zip(list1, list2)]
print(test_list)
print(new_list)

# digits =[]
# for i in date1:
#     if i.isdigit():
#         digits.append(i)

# print(digits)
# date1 = datetime.datetime(int(list_dates[1]))
# date2 = datetime.datetime(int(list_dates[2]))

# delta = date2 - date1
# print(delta)
