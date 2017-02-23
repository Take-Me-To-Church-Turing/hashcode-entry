from stream import *

def get_output_string(cache_servers):
    count = len(cache_servers)
    output = str(count) + "\n"

    for server in cache_servers:
        output += str(server.uid) + " "

        for video in server.videos:
            output += str(video.uid) + " "
        
        output += "\n"
    
    return output

# Testing
if __name__ == '__main__':
    server = CacheServer(3290, 100)
    server.videos = [Video(2, 100), Video(4, 200)]
    print(get_output_string([server]))