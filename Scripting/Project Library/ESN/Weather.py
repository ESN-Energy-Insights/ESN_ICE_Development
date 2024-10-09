	
def getWeather(tagpath):

	locpath = [tagpath+'/Weather/Location']
	qualifiedValues= system.tag.readBlocking(locpath)
	value = qualifiedValues[0]
	url = 'https://api.weather.gov/stations/'+value.value+'/observations/latest?require_qc=true'
	response = system.net.httpGet(url) 
	json=system.util.jsonDecode(response) 
	timestamp = json["properties"]["timestamp"]

	system.tag.writeBlocking(tagpath + "/Weather/temp", json["properties"]["temperature"]["value"])
	system.tag.writeBlocking(tagpath + "/Weather/timestamp", json["properties"]["timestamp"])
	system.tag.writeBlocking(tagpath + "/Weather/clouds", json["properties"]["cloudLayers"][0]["amount"])
	system.tag.writeBlocking(tagpath + "/Weather/humidity", json["properties"]["relativeHumidity"]["value"])
	system.tag.writeBlocking(tagpath + "/Weather/wind speed", json["properties"]["windSpeed"]["value"])
	
	return timestamp
