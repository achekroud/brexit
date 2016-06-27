import geojson
import matplotlib.pyplot as plt
from descartes import PolygonPatch
from pprint import pformat
dataLoc = open('wpc.json')
refjson = dataLoc.read()
json_data = geojson.loads(refjson)
x=[]
y=[]
'''
coords = json_data['features'][5]['geometry']['coordinates']
x += [i for i,j in coords[0]]
y += [j for i,j in coords[0]]
print coords
'''
wpcs = []
print len(json_data['features'])
for i in range(len(json_data['features'])):
    wpcs.append(json_data['features'][i]['properties']['PCON13NM'])
print len(wpcs)
nameToCoords={}
#print wpcs
for wpc in wpcs:
	for x in range(len(json_data['features'])):
		if json_data['features'][x]['properties']['PCON13NM']==wpc:
			nameToCoords[wpc]=json_data['features'][x]['geometry']['coordinates']
formatted = pformat (nameToCoords)
'''
locat = open('nameToCoordsFile', 'w')
locat.write(formatted)
'''
location = raw_input('Search your consituency')

coords= nameToCoords[location]
x=[i for i,j in coords[0]]
y=[j for i,j in coords[0]]
fig = plt.figure()
ax = fig.gca() 
ax.plot(x,y)
ax.axis('scaled')
plt.show()


