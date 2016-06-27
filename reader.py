import json, urllib2
from pprint import pprint
dataUrl = urllib2.urlopen('https://petition.parliament.uk/petitions/131215.json')
refJson = dataUrl.read()
refData = json.loads(refJson)
constitData = refData['data']['attributes']['signatures_by_constituency']


def constitValues(constitData):
    '''
    This is a function that will access the data and return a dictionary with 'constituencyName':'numberOfSignatures'
    '''
    constituencies = {}
    for item in constitData:
        constituencies[item.get('name')] = item.get('signature_count')
    return (constituencies)
