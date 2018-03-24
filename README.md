# meshping
Check a full mesh of hosts for network connectivity between them and export statistics for display.

## Probe
The probe is designed to be simple and aimed at a target of a [Raspberry Pi](https://www.raspberrypi.org/) or any system running Debian Linux.
It requires fping and python to be installed, and functional networking and DNS to talk to the outside world.

### Probe Prerequisites
* Ideally, a modern version of Debian on whatever device you want to use as a probe. A Raspberry Pi should work perfectly, or any server / computer, provided the number of hosts in your mesh is not too large.
* Python 3.0 *(or possibly earlier versions. I've not really tested a great deal.)*
* fping  *(If you don't have this, `apt-get install fping` should get you up and running.)*

## Interface
The interface provides some custom web visualisations for the data collected.
Alternatively, since the probe exports all data collected in [Prometheus format](https://prometheus.io/docs/instrumenting/exposition_formats/), you can simply point your prometheus server at the various probes and aggregate data to get time-series visualisations through [prometheus](https://prometheus.io/) or something like [Grafana](https://grafana.com/).

### Interface Prerequisites
No idea. Some kind of webserver. I'll try and keep things fairly minimalist, and allow power users to create custom graphs and dashboards with [Prometheus + Grafana](http://docs.grafana.org/features/datasources/prometheus/) or any of the alternatives out there.

## A warning about scaling
Since this system sends network traffic and gathers statistics between every pair of hosts in the mesh, this is a classic n<sup>2</sup> scaling problem. This works well when you have tens of hosts. You may need something more powerful than a [Raspberry Pi](https://www.raspberrypi.org/) as probes for hundreds of hosts, and if you have thousands of hosts, you're going to have a bad time.
