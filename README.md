# prometheus_clearwater
Monitoring and implamentation of __VIMS-ClearWater__ wich __Prometheus__, __Grafana__ and __containers-Exporters__

----------------

## NB: here you need to use only two files: docker-compose.yml and prometheus.yml


## Prerequisites
To start you need to install [__docker__ and __docker-compose__](https://websiteforstudents.com/how-to-install-docker-and-docker-compose-on-ubuntu-16-04-18-04/)

## Getting Started

We have used and docker-compose.yml
 
To create a volume  for grafana :  

`docker volume create --name=grafana-volume`

After, stay on projet repository and type:

`docker_compose up`

In the navigator, type:  

* `ip@:9090` to view prometheus Dashbord   
* and `ip@:3000` to view grafana Dashbord

# Contributing

We'd love for you to contribute to this container. You can request new features by creating an issue, or submit a pull request with your contribution.

