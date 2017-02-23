class Endpoint:
	
	def __init__(self, lines, startIndex):
		curLine = lines[startIndex]
		startIndex += 1
		self.datacenterLatency = curLine[0]
		self.numberOfCaches = curLine[1]
		self.cacheLatencies = {}
		for _ in range(self.numberOfCaches):
			curLine = lines[startIndex]
			startIndex += 1
			cacheIndex = curLine[0]
			cacheLatency = curLine[1]
			self.cacheLatencies[cacheIndex] = cacheLatency
		self.videoRequests = {}

	def getDatacenterLatency(self):
		return self.datacenterLatency

	def getNumberOfCaches(self):
		return self.numberOfCaches

	def getCacheLatencies(self):
		return self.cacheLatencies

	def getVideoRequests(self):
		return self.videoRequests

	def addVideoRequest(self, videoId, numberOfRequests):
		self.videoRequests[videoId] = numberOfRequests



with open('kittens.in', 'r') as f:
	lines = map(lambda line: map(int, line.split(" ")), f.readlines())


numberOfVideos = lines[0][0]
numberOfEndpoints = lines[0][1]
numberOfVideoRequests = lines[0][2]
numberOfCacheServers = lines[0][3]
cacheServerSize = lines[0][4]

videosSizes = lines[1]

endpoints = []
startIndex = 2
print(numberOfEndpoints)
for i in range(numberOfEndpoints):
	endpoints.append(Endpoint(lines, startIndex))
	startIndex += endpoints[i].getNumberOfCaches() + 1

for _ in range(numberOfVideoRequests):
	curLine = map(int, lines[startIndex])
	startIndex += 1
	endpoints[curLine[1]].addVideoRequest(curLine[0], curLine[2])

# print(numberOfVideos, numberOfEndpoints, numberOfVideoRequests, numberOfCacheServers, cacheServerSize)
# print(videosSizes)
# for i in range(numberOfEndpoints):
# 	print(endpoints[i].getDatacenterLatency(), endpoints[i].getCacheLatencies(), endpoints[i].getVideoRequests())
