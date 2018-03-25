''' This is the main entry point for the probe

It will:
1. Read configuration from its database (a text file)
2. Execute measurements as required (ping first, we'll add module support later, maybe)
3. Make those measurements available using prometheus style metrics on :9091/metrics (by default)

Later:
- Support configuration of additional nodes through the web api :9091/config
'''

# Definitions...
hostname = 'localhost'
webserver_port = 9091

# Set up a webserver so our metrics can be scraped...
from prometheus_client import start_http_server, Summary
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(random.random())

# PING TEST (point to point latency & packet loss) - will move this to its own file later...
# Fork out to fping (which must be installed)...

# host ping test : uses fping to sent 10 packets, gathers 10 responses and calculates packet loss, min/avg/max latency...
import subprocess
#response = subprocess.check_output("fping", "-C 10", "-i 1", "-p 500", "-t 2000", "-q", "-R", hostname)
# ping the host 10 times and gather 10x results which are either a latency value in ms, or -,
# which means packet was not returned within the timeout.
ping_cmd = (["fping", "-C 10", "-i 1", "-p 500", "-t 2000", "-q", "-R", hostname])

p = subprocess.Popen(ping_cmd, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
out, err = p.communicate()

# fping sends back statistics in stderr, since we specified -q...

exit
