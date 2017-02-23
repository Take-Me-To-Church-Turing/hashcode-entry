class CacheServer:
	uid = 0
	size = 0 # MB

	def __init__(uid, size):
		this.uid = uid
		this.size = size

class Endpoint:
	uid = 0
	cache_latencies = {}

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
