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

# PING TEST (point to point latency & packet loss)
# Fork out to fping (which must be installed)...

# host ping test : uses fping to sent 10 packets, gathers 10 responses and calculates packet loss, min/avg/max latency...
import subprocess
#response = subprocess.check_output("fping", "-C 10", "-i 1", "-p 500", "-t 2000", "-q", "-R", hostname)
ping_cmd = (["fping", "-C 10", "-i 1", "-p 500", "-t 2000", "-q", "-R", hostname])

p = subprocess.Popen(ping_cmd, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
out, err = p.communicate()

# fping sends back statistics in stderr, since we specified -q...
print(err)
exit
