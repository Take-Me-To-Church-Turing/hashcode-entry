from stream import *
from parser import *
from emitter import *

def run(caches, endpoints):
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

def test():
    caches = [Cache(0, 100), Cache(1, 100), Cache(2, 100)]
    videos = [Video(0, 50), Video(1, 50), Video(2, 80), Video(3, 30), Video(4, 110)]
    endpoints = [Endpoint(0, {caches[0]: 100, caches[1]: 200, caches[2]: 200}, {videos[1]:1000, videos[3]: 1500, videos[4]: 500}, 1000),
    			 Endpoint(1, {}, {videos[0]: 1000}, 500)]

    run(caches, endpoints)

def runWithParseTest():
    caches, endpoints = parse("test.in")
    run(caches, endpoints)

    print(get_output_string(caches))

if __name__ == '__main__':
	runWithParseTest()
