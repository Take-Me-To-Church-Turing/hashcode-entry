class CacheServer:
	uid = 0
	capacity = 0 # MB
	used = 0 # MB

	videos = []

	def __init__(self, uid, capacity):
		self.uid = uid
		self.capacity = capacity

class Endpoint:
	uid = 0
	cache_latencies = {}
	video_requests = {} # uid, num_requests
	datacenter_latency = 0

	def __init__(self, uid, cache_latencies):
		self.uid = uid
		self.cache_latencies = cache_latencies

class Video:
	uid = 0
	size = 0

	def __init__(self, uid, size):
		self.uid = uid
		self.size = size

def weight(endpoint, cache, video):
	pass

def get_priority_queue():
	pass
