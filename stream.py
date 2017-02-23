class CacheServer:
	uid = 0
	capacity = 0 # MB
	used = 0 # MB

	videos = []

	def __init__(uid, size):
		this.uid = uid
		this.capacity = capacity

class Endpoint:
	uid = 0
	cache_latencies = {}
	video_requests = {} # uid, num_requests
	datacenter_latency = 0

	def __init__(uid, cache_latencies):
		this.uid = uid
		this.cache_latencies = cache_latencies

class Video:
	uid = 0
	size = 0

	def __init__(uid, size):
		this.uid = uid
		this.size = size

def weight(endpoint, cache, video):
	pass

def get_priority_queue():
	pass
