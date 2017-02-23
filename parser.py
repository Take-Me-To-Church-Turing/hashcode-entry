from stream import Cache
from stream import Video
from stream import Endpoint

def parse(fileName):
	with open(fileName, 'r') as f:
		lines = map(lambda line: map(int, line.split(" ")), f.readlines())
	numberOfVideos = lines[0][0]
	numberOfEndpoints = lines[0][1]
	numberOfVideoRequests = lines[0][2]
	numberOfCacheServers = lines[0][3]
	cacheServerSize = lines[0][4]
	videosSizes = lines[1]

	endpoints = []
	startIndex = 2
	for i in range(numberOfEndpoints):
		endpoints.append(parseEndpoint(lines, startIndex))
		startIndex += len(endpoints[i][1]) + 1
	for _ in range(numberOfVideoRequests):
		curLine = lines[startIndex]
		startIndex += 1
		endpoints[curLine[1]][2][curLine[0]] = Video(curLine[0], curLine[2])

	cacheList = []
	endpointList = []
	for i in range(numberOfCacheServers):
		cacheList.append(Cache(i, cacheSize))

	for i in range(numberOfEndpoints):
		endpointList.append(Endpoint(i, endpoints[i][1], endpoints[i][2], endpoints[i][0]))
	

	return (cacheList, endpointList)


def parseEndpoint(lines, startIndex):
	returnValue = []

	curLine = lines[startIndex]
	startIndex += 1

	returnValue.append(curLine[0])
	returnValue.append({})

	numberOfCaches = curLine[1]
	for _ in range(numberOfCaches):
		curLine = lines[startIndex]
		startIndex += 1
		returnValue[1][curLine[0]] = curLine[1]
	returnValue.append({})

	print(returnValue)
	return returnValue