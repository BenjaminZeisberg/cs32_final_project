from click import secho
import folium
from csv import reader
import datetime
import re
from folium import plugins
from folium.plugins import HeatMap



#establishing map for each day
a = folium.Map(location=[42.36698,-71.12500], zoom_start = 10)
b = folium.Map(location=[42.36698,-71.12500], zoom_start = 10)
c = folium.Map(location=[42.36698,-71.12500], zoom_start = 10)
d = folium.Map(location=[42.36698,-71.12500], zoom_start = 10)
e = folium.Map(location=[42.36698,-71.12500], zoom_start = 10)
f = folium.Map(location=[42.36698,-71.12500], zoom_start = 10)
g = folium.Map(location=[42.36698,-71.12500], zoom_start = 10)
heat = folium.Map(location=[42.36698,-71.12500], zoom_start = 10)

# Data linked to each map
data_source = [(a,'data/2022-04-17.csv'), (b,'data/2022-04-18.csv'),(c, 'data/2022-04-19.csv'),(d, 'data/2022-04-20.csv'),(e,'data/2022-04-21.csv'), (f, 'data/2022-04-22.csv'), (g, 'data/2022-04-23.csv')]
#data_source = [(a,'data/2022-04-17.csv'), (b,'data/2022-04-18.csv')]

data_items = []
global_location = []
data_difference = []
location = []

for item in data_source:
    with open(item[1]) as data:
        csv_reader = reader(data)
        header = next(csv_reader)
        # reading it line by line! Same approach as we used when reading the CatInTheHat :)
        # we are skipping the first line. Since we dont want the header in our data, but want it to stay in the CSV file.
        if header != None:
            for row in csv_reader:
                if row[2] != '' and row[3] != '': 
                    # this is lat, long, time
                    location.append([row[2], row[3], row[1]])
                else:
                    pass


for i in range(0, len(location)):
    if i +1 < len(location):
        date1 = re.split('\ |:|-', location[i][2])
        date1.pop()

        date2 = re.split('\ |:|-', location[i+1][2])
        date2.pop()
 
        for items in date1:
            dic = {'year': date1[0], 'month': date1[1], 'day': date1[2], 'hour': date1[3], 'minute': date1[4], 'seconds': date1[5]}
            dic2 = {'year': date2[0], 'month': date2[1], 'day': date2[2], 'hour': date2[3], 'minute': date2[4], 'seconds': date2[5]}
        
        dt1 = datetime.datetime(int(dic['year']), int(dic['month']), int(dic['day']), int(dic['hour']), int(dic['minute']), int(dic['seconds']))
        dt2 = datetime.datetime(int(dic2['year']), int(dic2['month']), int(dic2['day']), int(dic2['hour']), int(dic2['minute']), int(dic2['seconds']))
        delta = abs(dt2 - dt1)
        data_difference.append(delta.total_seconds())
        # based off of the fact that we are subtracting the second from the first item our new list will be one item shorter than the gps data list. So we need to artificially create one additional point for the time.
        # can see this when running these two
        # since I know that our data starts at the 2022-04-17 I can artificially create one time data that starts at midnight. This is kind of correct since i was asleep in my bed at midnight at that gps marker
    if i == 0:
        dt0 = datetime.datetime(year=2022, month=4, day=17, hour=0, minute=0, second=1)
        dt0_2 = datetime.datetime(int(dic['year']), int(dic['month']), int(dic['day']), int(dic['hour']), int(dic['minute']), int(dic['seconds']))
        delta_2 = abs(dt0_2 - dt0)
        # now inserting the artificial data point to the beginning of the list
        data_difference.insert(0,delta_2.total_seconds()) 



x = 0
i = 0
marker_paths = []
count_marker = 0
for items in location:
    if x + 1 < len(location):
        date1 = re.split('\ |:|-', location[x][2])
        date2 = re.split('\ |:|-', location[x+1][2])

        if date1[2] == date2[2]:
            #print(date1, date2)
            time = "{:0>8}".format(str(datetime.timedelta(seconds=data_difference[x])))
            f_string = f"Time spent at this marker is: {time}"
            # f_string = f"Time spent at this marker is: 0.0{data_difference[0]}"
            html = f_string
            # html = '''
            # {%data_difference[0]%}<br>
            # 2nd line<br>
            # 3rd line'''
            iframe = folium.IFrame(html,
                                width=100,
                                height=100)

            popup = folium.Popup(iframe,
                                max_width=100)
            #paint marker, and then append the marker to the list of markers
            folium.Marker([float(items[0]), float(items[1])], popup=popup).add_to(data_source[i][0])
            marker_paths.append([float(items[0]), float(items[1])])

            if len(marker_paths) != 1:
                start = marker_paths[count_marker][0], marker_paths[count_marker][1]
                end = marker_paths[count_marker+1][0], marker_paths[count_marker+1][1]
                locations = [start, end]
                folium.PolyLine(locations, color='green', weight=7, opacity=0.5).add_to(data_source[i][0])
                count_marker += 1 
            else: 
                pass

        elif date1[2] != date2[2]:
            folium.Marker([float(items[0]), float(items[1])], popup=popup).add_to(data_source[i][0])
            marker_paths.append([float(items[0]), float(items[1])])
            # save the map as html
            data_source[i][0].save(f'templates/map{i}.html')
            i += 1
        if i == 6:
            # this is making sure we save the last map. Since we are checking for the dates, in the elif before
            data_source[i][0].save(f'templates/map{i}.html')
    x += 1

data_choro = []
# newlist = [location+data_difference for location, data_difference in zip(location, data_difference)]
a = 0

for items in location:
    data_choro.append([float(items[0]), float(items[1]), data_difference[a]])
    a += 1


# for items in data_choro:
#     HeatMap(items).add_to(heat)
gradient_test = {0.4: 'blue', 0.65: 'lime', 1: 'red'}

HeatMap(data_choro, radius=20, blur=0.5).add_to(heat)

data_source.append((heat, '0'))

#add the heatmap to the list of maps so I can simply call it using the function below.

# heat.save('heat_map.html')

# using list comprehension to combine the two lists

def return_map(a):
    return data_source[a][0]