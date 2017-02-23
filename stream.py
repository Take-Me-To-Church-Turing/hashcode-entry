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
	cache_latencies = {} # cache uid, latency.  You probably want delta_latencies
	delta_latencies = {} # cache uid, delta latency
	video_requests = {} # video uid, num_requests
	datacenter_latency = 0

	def __init__(self, uid, cache_latencies, video_requests, datacenter_latency):
		self.uid = uid
		self.cache_latencies = cache_latencies
		self.video_requests = video_requests
		self.datacenter_latency = datacenter_latency

		self.compute_delta_latencies()

	def compute_delta_latencies(self):
		for uid, cache_latency in self.cache_latencies.items():
			self.delta_latencies[uid] = self.datacenter_latency - cache_latency

class Video:
	uid = 0
	size = 0

	def __init__(self, uid, size):
		self.uid = uid
		self.size = size

def weight(endpoint, cache, video):
	# num_requests * (datacenter latency - cache latency) / video_size

	num_requests = endpoint.video_requests[video.uid]
	delta_latency = endpoint.delta_latencies[cache.uid]
	video_size = video.size

	return num_requests * delta_latency / video_size


def test_weight():
	sample_cache = CacheServer(1, 1000)
	sample_endpoint = Endpoint(1, {1: 100}, {1: 50}, 500)
	sample_video = Video(1, 500)

	print(weight(sample_endpoint, sample_cache, sample_video))

test_weight()

