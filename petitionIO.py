import json
def fileIO(file):
	data = open(file)
	refjson = data.read()
	json_data = json.loads(refjson)
	return json_data
def maxminValue(file):
	'''
	This function takes the location/url and returns the max and min number of signatures for any 1 constituency
	'''
	json_data=fileIO(file)
	return max([json_data['data']['attributes']['signatures_by_constituency'][x]['signature_count'] for x in range(len(json_data['data']['attributes']['signatures_by_constituency']))]), min([json_data['data']['attributes']['signatures_by_constituency'][x]['signature_count'] for x in range(len(json_data['data']['attributes']['signatures_by_constituency']))])


def constitValue(constit , file):
	'''
	returns the number of signatures for the constituency specified
	constit: the constituency that is searched
	'''
	json_data=fileIO(file)
	for x in range(len(json_data['data']['attributes']['signatures_by_constituency'])):
		if constit == json_data['data']['attributes']['signatures_by_constituency'][x]['name'].replace(',',''):
			return int(json_data['data']['attributes']['signatures_by_constituency'][x]['signature_count'])
			

