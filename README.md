# prometheus_clearwater
Monitoring Containers __VIMS-ClearWater__ with __Prometheus__, __Grafana__ and __containers-Exporters__

----------------

## NB: here you need to use only two files: docker-compose.yml and prometheus.yml


## Prerequisites
To start you need to install [__docker__ and __docker-compose__](https://websiteforstudents.com/how-to-install-docker-and-docker-compose-on-ubuntu-16-04-18-04/)
You also need to pull the docker images of: [_prometheus_](https://hub.docker.com/r/prom/prometheus/), [grafana](https://hub.docker.com/r/grafana/grafana/) and [container-exporter](https://hub.docker.com/r/prom/container-exporter/) 

## Getting Started

We have used and docker-compose.yml
 
To create a volume for grafana :  

`docker volume create --name=grafana-volume`

On a terminal type:

`docker_compose up`

In a browser, type:  

* `localhost@:9090` for prometheus Dashbord   
* and `localhost@:3000` for grafana Dashbord

## Storage

A script in python which copy the metrics from Prometheus to a file, is available on __readwrite.py__   
We have chosed to work with __CVS file__. The extension file CVS (Comma-Separated Values)  is a text file that serves as a swap file between different software, most commonly between a spread sheet and another program. It allows to get rid of proprietary file formats, often complex, and unknown to other software.

# References

- [Prometheus].https://github.com/prometheus/prometheus
- [Clearwater-docker].https://github.com/cherrared/clearwater-docker
- [Prometheus-remote-storage].https://github.com/gdmello/prometheus-remote-storage

# Contributing

We'd love for you to contribute to this container. You can request new features by creating an issue, or submit a pull request with your contribution.

