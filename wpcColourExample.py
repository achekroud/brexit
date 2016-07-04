import geojson
import matplotlib.pyplot as plt
from petitionIO import maxminValue, constitValue
from colour import Color
from math import ceil

'''
Author: Ross Williams
Email: r.d.williams1993(at)gmail.com

Thanks to: https://github.com/martinjc/UK-GeoJSON For the ukGeoJSON data for Westminster parliamentary constituencies (WPC)

This is an example program that will allow you to enter your constituency and will produce an outline of the constituency and a colour ranging white to red based on how many people signed the petition, compared to the constituency with the largest number of signatures.

TODO: make it a chloropleth UK map, (at the moment this would be possible but the number of data points is too large to handle i think)
'''
geoDataLoc = open('wpc.json')
refjson = geoDataLoc.read()
json_data = geojson.loads(refjson)
x=[]
y=[]
location = raw_input('Search your consituency: ').replace(' ','').replace(' ','').lower()
maxValue, minValue = maxminValue('euReferendum.json')
currentVal = float(constitValue(location, 'euReferendum.json'))

colourNo = int(ceil((currentVal/maxValue)*632))

red = Color("red")
white = Color("white")
colouring = list(white.range_to(red, 632))
mapCol= str(colouring[colourNo])

currentValue = constitValue(location, 'euReferendum.json')
nameToCoords={}

for x in range(len(json_data['features'])):
		if location == json_data['features'][x]['properties']['PCON13NM'].replace(',','').replace(' ','').lower():
			nameToCoords[location]=json_data['features'][x]['geometry']['coordinates']

coords= nameToCoords[location]
x=[i for i,j in coords[0]]
y=[j for i,j in coords[0]]
fig = plt.figure()
ax = fig.gca() 
ax.plot(x,y)
ax.axis('scaled')
ax.fill_between(x,y, facecolor=mapCol, alpha=0.5)
plt.show()


