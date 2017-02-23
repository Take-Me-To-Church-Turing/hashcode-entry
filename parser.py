from stream import Cache
from stream import Video
from stream import Endpoint

def parse(fileName):
	with open(fileName, 'r') as f:
		lines = list(map(lambda line: list(map(int, line.split(" "))), f.readlines()))
	numberOfVideos = lines[0][0]
	numberOfEndpoints = lines[0][1]
	numberOfVideoRequests = lines[0][2]
	numberOfCacheServers = lines[0][3]
	cacheServerSize = lines[0][4]
	videosSizes = lines[1]
	
	cacheList = []
	for i in range(numberOfCacheServers):
		cacheList.append(Cache(i, cacheServerSize))

	videoList = []
	for i in range(numberOfVideos):
		videoList.append(Video(i, videosSizes[i]))

	endpoints = []
	startIndex = 2
	for i in range(numberOfEndpoints):
		endpoints.append(parseEndpoint(lines, startIndex, cacheList))
		startIndex += len(endpoints[i][1]) + 1

	for _ in range(numberOfVideoRequests):
		curLine = lines[startIndex]
		startIndex += 1
		endpoints[curLine[1]][2][videoList[curLine[0]]] = curLine[2] 

	endpointList = []

	for i in range(numberOfEndpoints):
		endpointList.append(Endpoint(i, endpoints[i][1], endpoints[i][2], endpoints[i][0]))
	
	return (cacheList, endpointList)


def parseEndpoint(lines, startIndex, caches):
	returnValue = []

	curLine = lines[startIndex]
	startIndex += 1

	returnValue.append(curLine[0])
	returnValue.append({})

	numberOfCaches = curLine[1]
	for _ in range(numberOfCaches):
		curLine = lines[startIndex]
		startIndex += 1
		returnValue[1][caches[curLine[0]]] = curLine[1]
	returnValue.append({})

	return returnValue