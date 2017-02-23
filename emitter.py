from stream import *

def get_output_string(cache_servers):
    len = len(cache_servers)
    output = len + "\n"
    
    for server in cache_servers:
        output += server.uid + " "

        for video in server.videos:
            output += video.uid + " "
        
        output += "\n"
    
    return output