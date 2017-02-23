class CacheServer:
	uid = 0
	capacity = 0 # MB
	used = 0 # MB

	cached_videos = []

	def __init__(self, uid, capacity):
		self.uid = uid
		self.capacity = capacity

class Endpoint:
	uid = 0
	cache_latencies = {} # cache, latency.  You probably want delta_latencies
	delta_latencies = {} # cache, delta latency
	video_requests = {} # video, num_requests
	datacenter_latency = 0

	def __init__(self, uid, cache_latencies, video_requests, datacenter_latency):
		self.uid = uid
		self.cache_latencies = cache_latencies
		self.video_requests = video_requests
		self.datacenter_latency = datacenter_latency

		self.compute_delta_latencies()

	def compute_delta_latencies(self):
		for cache, cache_latency in self.cache_latencies.items():
			self.delta_latencies[cache] = self.datacenter_latency - cache_latency

	def make_unsorted_queue(self, cache):
		unsorted = {}

		for video, num_requests in self.video_requests.items():
			unsorted[video] = weight(self, cache, video)

		return unsorted

class Video:
	uid = 0
	size = 0

	def __init__(self, uid, size):
		self.uid = uid
		self.size = size

def weight(endpoint, cache, video):
	# num_requests * (datacenter latency - cache latency) / video_size

	num_requests = endpoint.video_requests[video]
	delta_latency = endpoint.delta_latencies[cache]
	video_size = video.size

	return num_requests * delta_latency / video_size


def test():
	caches = [CacheServer(0, 1000)]
	videos = [Video(0, 500)]
	endpoints = [Endpoint(0, {caches[0]: 100}, {videos[0]: 50}, 500)]

	print(weight(endpoints[0], caches[0], videos[0]))

	print(endpoints[0].make_unsorted_queue(caches[0]))

test()

