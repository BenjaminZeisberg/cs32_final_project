import folium
from csv import reader
#Data 

with open('tracks (1).csv') as data:
    location = []
    csv_reader = reader(data)
    header = next(csv_reader)
    # reading it line by line! Same approach as we used when reading the CatInTheHat :)
    # we are skipping the first line. Since we dont want the header in our data, but want it to stay in the CSV file.
    if header != None:
        for row in csv_reader:
            if row[2] != '' and row[3] != '': 
                location.append([row[2], row[3]])
            else:
                pass

#Testing data -> Putting a marker for every collected GPS data point.

#establishing map
m = folium.Map(location=[42.36698,-71.12500], zoom_start = 5)
tooltip = "Click me!"

#start point for the day

folium.Marker([42.37882,-71.12420], popup="<i>Start</i>", tooltip=tooltip).add_to(m)

marker_paths = []
for items in location:
    folium.Marker([float(items[0]), float(items[1])], popup="Data points", tooltip=tooltip).add_to(m)
    marker_paths.append([float(items[0]), float(items[1])])

for i in range(0,len(marker_paths)):
    if i+2 > len(marker_paths):
        pass
    else:
        # we have to order the data to match the needed input for the PolyLine function
        start = marker_paths[i][0], marker_paths[i][1]
        end = marker_paths[i+1][0], marker_paths[i+1][1]

        #giving the line the coordinates
        locations = [start, end]
        folium.PolyLine(locations, color='green', weight= 10, opacity=0.5).add_to(m)
m



