from backend import location, data_items
import datetime
import folium
from folium import plugins
from folium.plugins import HeatMap
import re
# we need a function that when given a lat,long it returns us four coordinates for the rectangle polygon shape, which is needed for the geojson file
# we know from here https://www.usna.edu/Users/oceano/pguth/md_help/html/approx_equivalents.htm that 0.000001 change in long, or lat results in 10m change. This will be the radius of our

a = folium.Map(location=[42.36698,-71.12500], zoom_start = 10)

# for items in locations_seconds:


data_difference = []
data_difference_seconds = []
for i in range(0, len(data_items)):
    if i == 0:
        pass
    elif i + 1 < len(data_items):
        # this allows us to split the data at the certain points so we can put it into datatime
        date1 = re.split('\ |:|-', data_items[i])
        date2 = re.split('\ |:|-', data_items[i+1])
        date1.pop()
        date2.pop()
        
    # rearranging in the form of a dictionary so that we can use the datatime.datatime class
for items in date1:
    dic = {'year': date1[0], 'month': date1[1], 'day': date1[2], 'hour': date1[3], 'minute': date1[4], 'seconds': date1[5]}
    dic2 = {'year': date2[0], 'month': date2[1], 'day': date2[2], 'hour': date2[3], 'minute': date2[4], 'seconds': date2[5]}


    dt1 = datetime.datetime(int(dic['year']), int(dic['month']), int(dic['day']), int(dic['hour']), int(dic['minute']), int(dic['seconds']))
    dt2 = datetime.datetime(int(dic2['year']), int(dic2['month']), int(dic2['day']), int(dic2['hour']), int(dic2['minute']), int(dic2['seconds']))

    #we apply the abs() function here since we don't want to include negative values here. This happens when we go from one day marker to the next day marker. e.g. a datapoint like 20:02:03 PM to 06:50:00 AM
    delta = abs(dt2 - dt1)
    data_difference.append(delta.total_seconds())
    
    # Using list comprehension to add the time to the location list. Thank StackOverflow for the help. 
print(len(location))
print(len(data_difference))     

for items in range(0,len(location)):
    location[i].append(data_difference[i])
print(location)
