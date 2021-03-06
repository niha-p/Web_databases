import urllib2
import base64
import json

def ping(site,query,key):
	
	bingUrl = 'https://api.datamarket.azure.com/Data.ashx/Bing/SearchWeb/v1/Composite?Query=%27site%3a'+ site +'%20'+ query +'%27&$top=4&$format=json'
	accountKey = key	
	top4=[]
	accountKeyEnc = base64.b64encode(accountKey + ':' + accountKey)
	headers = {'Authorization': 'Basic ' + accountKeyEnc}
	req = urllib2.Request(bingUrl, headers = headers)
	response = urllib2.urlopen(req)
	content = response.read()

	#content contains the xml/json response from Bing. 
	bingweb = json.loads(content)['d']['results'][0]

	for i in bingweb['Web']:
		url = i['Url']
		url = url.encode("ascii", "ignore")
		top4.append(url)

	return int(bingweb['WebTotal']), top4
