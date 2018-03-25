# PING TEST (point to point latency & packet loss)
# Fork out to fping (which must be installed)...

# host ping test : uses fping to sent 10 packets, gathers 10 responses and calculates packet loss, min/avg/max latency...
import subprocess
import re

# Note that this function can take some time to return, particularly if latency /
# packetloss to the target host is high.
# TODO: make calls to ping() parallelisable and return asynchronously

def ping(hostname):
    #response = subprocess.check_output("fping", "-C 10", "-i 1", "-p 500", "-t 2000", "-q", "-R", hostname)
    # ping the host 10 times and gather 10x results which are either a latency value in ms, or -,
    # which means packet was not returned within the timeout.
    ping_cmd = (["fping", "-C 10", "-i 1", "-p 500", "-t 2000", "-q", "-R", hostname])

    p = subprocess.Popen(ping_cmd, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    out, err = p.communicate()

    if(out != 0):
        # some error occurred with fping, such as DNS resolution, host doesn't exist, etc.
        # We return some values since we don't want an error to stop other tests...
        return float('NaN'), float('NaN'), float('NaN'), 10, 100

    # fping sends back statistics in stderr, since we specified -q...
    # Remove the hostname at the start of the string...
    latency_values = re.sub('^.*: ', '', err)

    # Split the 10 values we get, space separated...
    latencies = re.split(' ', latency_values)

    # Reset our counters for this host test instance...
    packets_total = 0
    latency_min = float(0)
    latency_avg = float(0)
    latency_max = float(0)
    latency_sum = float(0)
    packets_lost = 0
    packetloss_percent = float(0)

    for val in latencies:
        packets_total += 1
        if(val == '-'):
            packets_lost += 1
        else:
            # We need to handle min specially...
            if(latency_min == 0): latency_min = float(val)
            if(float(val) < latency_min): latency_min = float(val)
            if(float(val) > latency_max): latency_max = float(val)
            latency_sum += float(val)

    latency_avg = latency_sum / (packets_total - packets_lost)
    packetloss_percent = packets_lost / packets_total

    # Return content for export as metrics. Note that we return the hostname so
    # it will be easier to deal with asynchronous function return later on...
    return hostname, latency_min, latency_avg, latency_max, packets_lost, packetloss_percent, packets_total
