class Cache:
    def __init__(self, uid, capacity):
        self.uid = uid
        self.capacity = capacity
        self.used = 0
        self.cached_videos = []
        self.cached_video_priority_queue = [] # (video * (benefit * endpoints)) list
        self.cached_video_benefit_dict = {} # video:[benefit, endpoints]

    def populate_priority_queue(self):
        self.cached_video_priority_queue = []
        self.cached_video_priority_queue = list(self.cached_video_benefit_dict.items())
        self.cached_video_priority_queue.sort(key=lambda i: i[1][0], reverse=True)

    def fill_cache(self):
        for (video, (benefit, endpoints)) in self.cached_video_priority_queue:
            if (self.used + video.size > self.capacity):
                continue
            self.cached_videos.append(video)
            self.used += video.size
        

class Endpoint:
    def __init__(self, uid, cache_latencies, video_requests, datacenter_latency):
        self.uid = uid
        self.caches = cache_latencies.keys()
        self.video_requests = video_requests # video, num_requests
        self.datacenter_latency = datacenter_latency
        self.unsorted_cache_video_benefits = {} # (cache-(video-benefit dictionary) dictionary)
        self.delta_latencies = {} # cache, delta latency

        self.compute_delta_latencies(cache_latencies)

    def compute_delta_latencies(self, cache_latencies):
        for cache, cache_latency in cache_latencies.items():
            self.delta_latencies[cache] = self.datacenter_latency - cache_latency

    def compute_unsorted_cache_video_benefits(self):
        caches = self.delta_latencies.keys()
        for cache in caches:
            video_benefits = {}

            for video, num_requests in self.video_requests.items():
                video_benefits[video] = self.video_weight_per_cache(cache, video)
            
            self.unsorted_cache_video_benefits[cache] = video_benefits
        
        return self.unsorted_cache_video_benefits

    def video_weight_per_cache(self, cache, video):
        # num_requests * (datacenter latency - cache latency) / video_size

        num_requests = self.video_requests[video]
        delta_latency = self.delta_latencies[cache]
        video_size = video.size

        return num_requests * delta_latency / video_size

class Video:
    def __init__(self, uid, size):
        self.uid = uid
        self.size = size

    def __repr__(self):
        return "Video({}, {})".format(self.uid, self.size)

def test():
    caches = [Cache(0, 100), Cache(1, 100), Cache(2, 100)]
    videos = [Video(0, 50), Video(1, 50), Video(2, 80), Video(3, 30), Video(4, 110)]
    endpoints = [Endpoint(0, {caches[0]: 100, caches[1]: 200, caches[2]: 200}, {videos[1]:1000, videos[3]: 1500, videos[4]: 500}, 1000),
    			 Endpoint(1, {}, {videos[0]: 1000}, 500)]

    # Combine endpoints
    for endpoint in endpoints:
        unsorted_cache_video_benefits = endpoint.compute_unsorted_cache_video_benefits()
        for cache, video_benefits in unsorted_cache_video_benefits.items():
            for video, benefit in video_benefits.items():
                if video in cache.cached_video_benefit_dict:
                    current_benefit = cache.cached_video_benefit_dict[video]
                    current_benefit[0] += benefit
                    current_benefit[1].append(endpoint)
                else:
                    cache.cached_video_benefit_dict[video] = [benefit, [endpoint]]
    # Now convert caches[i].cached_video_benefit_dict to ordered list

    for cache in caches:
        cache.populate_priority_queue()
        cache.fill_cache()



if __name__ == '__main__':
	test()
